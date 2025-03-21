import requests
import streamlit as st

# API URL
api_url = "https://requirements-wwub.onrender.com/predict"  # Replace with your actual Render API URL

st.title("T&G Tactics - Player Injury Risk Prediction ⚽🚑")

# Player Input Fields
player_name = st.text_input("Enter Player Name")
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=180)
weight = st.number_input("Weight (kg)", min_value=40, max_value=150, value=75)
pace = st.number_input("Pace (Speed)", min_value=0, max_value=99, value=80)
cumulative_minutes = st.number_input("Cumulative Minutes Played", min_value=0, value=5000)
avg_days_injured = st.number_input("Average Days Injured (Previous Seasons)", min_value=0, value=10)

# Predict Button
if st.button("Predict Injury Risk"):
    data = {"features": [height, weight, pace, cumulative_minutes, avg_days_injured]}

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            result = response.json()
            injury_risk = result.get("injury_risk", 0)

            if injury_risk == 1:
                st.warning(f"{player_name} is at HIGH RISK of injury! 🚑")
                st.write("🔹 **Recommended Tactical Adjustments:**")
                st.write("✅ Reduce playing time")
                st.write("✅ Focus on recovery and light training")
                st.write("✅ Consider substituting during second half")
            else:
                st.success(f"{player_name} is at LOW RISK of injury ✅")
                st.write("🔹 No special adjustments needed.")
        else:
            st.error("Failed to get response from API. Please check the server.")

    except requests.exceptions.RequestException as e:
        st.error(f"API Connection Error: {e}")
]