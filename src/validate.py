import re

# Specific Rwandan plate format (e.g., RAA123A)
PLATE_RE = re.compile(r'[A-Z]{3}[0-9]{3}[A-Z]')

def extract_valid_plate(text):
    text = text.upper().replace(" ", "").replace("-", "")
    m = PLATE_RE.search(text)
    if m:
        return m.group(0)
    return None
