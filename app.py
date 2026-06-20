

import streamlit as st

from detector import detect_diseases
from schedule import get_schedule
from food_db import get_food_recommendations
from parser import parse_report_text
from db import save_report, get_history
from utils import extract_text_from_image, extract_text_from_pdf
from ai_explainer import explain_report

st.set_page_config(page_title="HealthPath AI", layout="wide")

st.title("🩺 HealthPath AI - Patient Health Assistant")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Menu",
    ["Analyze Report", "Weekly Plan", "Insights", "History"]
)

data = {}

# ---------------- ANALYZE REPORT ----------------
if menu == "Analyze Report":

    st.subheader("📤 Upload or Enter Health Report")

    mode = st.radio("Input Method", ["Upload Report", "Manual Entry"])

    # -------- Upload Mode --------
    if mode == "Upload Report":
        file = st.file_uploader("Upload PDF / Image", type=["png", "jpg", "jpeg", "pdf"])

        if file:
            if file.type == "application/pdf":
                text = extract_text_from_pdf(file)
            else:
                text = extract_text_from_image(file)

            st.text_area("Extracted Report Text", text, height=200)

            data = parse_report_text(text)

            st.subheader("📊 Extracted Values")
            st.json(data)

    # -------- Manual Mode --------
    else:
        st.write("Enter your report values:")

        data["sugar"] = st.number_input("Fasting Sugar (mg/dL)", value=0.0)
        data["hba1c"] = st.number_input("HbA1c (%)", value=0.0)
        data["hemoglobin"] = st.number_input("Hemoglobin (g/dL)", value=0.0)
        data["cholesterol"] = st.number_input("Cholesterol (mg/dL)", value=0.0)
        data["bp"] = st.number_input("Blood Pressure (Systolic)", value=0.0)

    # -------- Analysis Button --------
    if st.button("Generate Health Plan"):

        diseases = detect_diseases(data)

        save_report(data, diseases)

        # HEALTH SCORE (safe wellness metric)
        health_score = max(0, 100 - len(diseases) * 15)

        st.subheader("📊 Health Summary")

        if not diseases:
            st.success("✅ No major issues detected. You are in healthy range.")
        else:
            st.warning(f"⚠️ Detected Conditions: {', '.join(diseases)}")

        st.metric("🌿 Wellness Score", f"{health_score}/100")

        # AI Explanation
        st.subheader("🧠 Health Explanation")
        st.info(explain_report(diseases, data))

        # Schedule
        st.subheader("📅 Daily Schedule")
        schedule = get_schedule(diseases)
        for time, activity in schedule.items():
            st.write(f"**{time}** → {activity}")

        # Food Plan
        st.subheader("🍎 Food Recommendations")
        food = get_food_recommendations(diseases)
        st.write(food)


# ---------------- WEEKLY PLAN ----------------
elif menu == "Weekly Plan":

    st.subheader("📅 7-Day Health Improvement Plan")

    base_schedule = get_schedule([])

    week = {
        "Monday": base_schedule,
        "Tuesday": base_schedule,
        "Wednesday": base_schedule,
        "Thursday": base_schedule,
        "Friday": base_schedule,
        "Saturday": base_schedule,
        "Sunday": {"Rest": "Light walk, hydration, relaxation"}
    }

    for day, plan in week.items():
        st.markdown(f"### {day}")
        st.write(plan)


# ---------------- INSIGHTS ----------------
elif menu == "Insights":

    st.subheader("📌 Health Insights Dashboard")

    history = get_history()

    total = len(history)

    st.metric("Total Reports Analyzed", total)

    if history:
        latest = history[0]

        st.subheader("🧾 Latest Report Snapshot")
        st.write(latest)

        st.info("Your system is tracking health history for better insights over time.")


# ---------------- HISTORY ----------------
elif menu == "History":

    st.subheader("📜 Patient History")

    history = get_history()

    if not history:
        st.info("No records found yet.")
    else:
        for record in history:
            st.write(record)
