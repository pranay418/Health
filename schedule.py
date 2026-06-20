
def get_schedule(diseases):
    base = {
        "06:30 AM": "Wake up and drink water",
        "07:00 AM": "Light exercise",
        "08:00 AM": "Healthy breakfast",
        "11:00 AM": "Fruit / hydration",
        "01:00 PM": "Balanced lunch",
        "05:00 PM": "Walk / snack",
        "08:00 PM": "Light dinner",
        "10:00 PM": "Sleep"
    }

    if not diseases:
        base["NOTE"] = "No issues detected. Maintain healthy lifestyle."
        return base

    if "Diabetes" in diseases:
        base["07:00 AM"] = "30 min brisk walk"
        base["08:00 AM"] = "Low sugar breakfast"

    if "Anemia" in diseases:
        base["08:00 AM"] = "Iron-rich breakfast"

    if "High Cholesterol" in diseases:
        base["01:00 PM"] = "Low fat diet"

    if "Hypertension" in diseases:
        base["05:00 PM"] = "Breathing exercises"

    return base
