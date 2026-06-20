
import re

def parse_report_text(text):
    data = {}

    sugar = re.search(r"(?:sugar|glucose)[^\d]*(\d+)", text, re.I)
    hba1c = re.search(r"HbA1c[^\d]*(\d+\.?\d*)", text, re.I)
    hb = re.search(r"(?:hemoglobin|hb)[^\d]*(\d+\.?\d*)", text, re.I)
    chol = re.search(r"(?:cholesterol)[^\d]*(\d+)", text, re.I)
    bp = re.search(r"(\d{2,3})\s*/\s*(\d{2,3})", text)

    if sugar:
        data["sugar"] = float(sugar.group(1))
    if hba1c:
        data["hba1c"] = float(hba1c.group(1))
    if hb:
        data["hemoglobin"] = float(hb.group(1))
    if chol:
        data["cholesterol"] = float(chol.group(1))
    if bp:
        data["bp"] = float(bp.group(1))

    return data
