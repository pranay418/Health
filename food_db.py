
def get_food_recommendations(diseases, veg=True):
    foods = {
        "Diabetes": ["Oats", "Sprouts", "Vegetables"],
        "Anemia": ["Spinach", "Pomegranate", "Dates"],
        "High Cholesterol": ["Oats", "Nuts", "Fruits"],
        "Hypertension": ["Banana", "Leafy vegetables"]
    }

    if not diseases:
        return ["Balanced diet: fruits, vegetables, proteins"]

    result = []
    for d in diseases:
        result.extend(foods.get(d, []))

    return list(set(result))
