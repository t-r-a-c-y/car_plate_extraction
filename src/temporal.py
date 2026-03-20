import cv2
import numpy as np
import time
import csv
import os
from collections import Counter

from detect import find_plate_candidates
from align import warp_plate
from ocr import read_plate_text
from validate import extract_valid_plate

BUFFER_SIZE = 5
COOLDOWN = 10   # seconds
CSV_FILE = "data/plates.csv"

def ensure_csv_exists():
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Plate Number", "Timestamp"])

def majority_vote(buffer):
    if not buffer:
        return None
    return Counter(buffer).most_common(1)[0][0]

def main():
    ensure_csv_exists()
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Camera not opened")

    plate_buffer = []
    last_saved_plate = None
    last_saved_time = 0

    print("Pipeline started. Press 'q' to quit.")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        vis = frame.copy()
        candidates = find_plate_candidates(frame)

        if candidates:
            # Pick the largest candidate
            rect = max(candidates, key=lambda r: r[1][0] * r[1][1])
            box = cv2.boxPoints(rect).astype(int)
            cv2.polylines(vis, [box], True, (0, 255, 0), 2)

            plate_img = warp_plate(frame, rect)
            raw_text = read_plate_text(plate_img)
            valid_plate = extract_valid_plate(raw_text)

            if valid_plate:
                plate_buffer.append(valid_plate)
                if len(plate_buffer) > BUFFER_SIZE:
                    plate_buffer.pop(0)

                confirmed_plate = majority_vote(plate_buffer)

                x = int(np.min(box[:, 0]))
                y = int(np.min(box[:, 1])) - 10
                
                cv2.putText(
                    vis,
                    f"CONFIRMED: {confirmed_plate}",
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

                now = time.time()
                if (
                    confirmed_plate
                    and confirmed_plate != last_saved_plate
                    and (now - last_saved_time) > COOLDOWN
                ):
                    with open(CSV_FILE, "a", newline="") as f:
                        writer = csv.writer(f)
                        writer.writerow([
                            confirmed_plate,
                            time.strftime("%Y-%m-%d %H:%M:%S")
                        ])

                    print(f"[SAVED] {confirmed_plate}")
                    last_saved_plate = confirmed_plate
                    last_saved_time = now

        cv2.imshow("Temporal Validation", vis)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
