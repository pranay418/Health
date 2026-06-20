
def explain_report(diseases, data):
    explanations = []

    if not diseases:
        return "Your report looks normal based on analyzed values. Maintain a healthy lifestyle."

    if "Diabetes" in diseases:
        explanations.append(
            "Your blood sugar levels are higher than normal. This means your body may not be processing sugar efficiently."
        )

    if "Anemia" in diseases:
        explanations.append(
            "Your hemoglobin level is low. This may reduce oxygen flow in your body and cause fatigue."
        )

    if "High Cholesterol" in diseases:
        explanations.append(
            "Your cholesterol level is elevated. This may be linked to diet and lifestyle habits."
        )

    if "Hypertension" in diseases:
        explanations.append(
            "Your blood pressure is higher than normal, which may be linked to stress or lifestyle factors."
        )

    return "\n\n".join(explanations)
