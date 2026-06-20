
def detect_diseases(data):
    diseases = []

    sugar = data.get("sugar", 0)
    hba1c = data.get("hba1c", 0)
    hb = data.get("hemoglobin", 0)
    cholesterol = data.get("cholesterol", 0)
    bp = data.get("bp", 0)

    if sugar > 126 or hba1c >= 6.5:
        diseases.append("Diabetes")

    if hb < 13:
        diseases.append("Anemia")

    if cholesterol > 240:
        diseases.append("High Cholesterol")

    if bp > 140:
        diseases.append("Hypertension")

    return diseases
