import cv2
import numpy as np

W_OUT, H_OUT = 450, 140

def order_points(pts):
    pts = np.array(pts, dtype=np.float32)
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1)

    top_left = pts[np.argmin(s)]
    bottom_right = pts[np.argmax(s)]
    top_right = pts[np.argmin(diff)]
    bottom_left = pts[np.argmax(diff)]

    return np.array(
        [top_left, top_right, bottom_right, bottom_left],
        dtype=np.float32
    )

def warp_plate(frame, rect):
    box = cv2.boxPoints(rect)
    src = order_points(box)

    dst = np.array([
        [0, 0],
        [W_OUT - 1, 0],
        [W_OUT - 1, H_OUT - 1],
        [0, H_OUT - 1]
    ], dtype=np.float32)

    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(frame, M, (W_OUT, H_OUT))

    return warped
