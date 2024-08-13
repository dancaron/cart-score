import streamlit as st

# Function to calculate CART Score
def calculate_cart_score(age, systolic_bp, heart_rate, respiration_rate, GCS):
    score = 0
    
    # Age score
    if age >= 65:
        score += 1
    
    # Systolic Blood Pressure score
    if systolic_bp < 90:
        score += 2
    elif systolic_bp < 120:
        score += 1
    
    # Heart Rate score
    if heart_rate > 110:
        score += 1
    
    # Respiration Rate score
    if respiration_rate > 30:
        score += 1
    
    # Glasgow Coma Scale score
    if GCS < 8:
        score += 2
    elif GCS <= 12:
        score += 1
    
    return score

# App description
st.title("CART (Cardiac Arrest Risk Triage) Score Calculator")
st.write("""
This application calculates the CART score, which is used to assess the risk of cardiac arrest in patients. The score is based on patient data including age, systolic blood pressure, heart rate, respiration rate, and Glasgow Coma Scale (GCS). The higher the score, the greater the risk of cardiac arrest.
""")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=65)
systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=50, max_value=250, value=120)
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=70)
respiration_rate = st.number_input("Respiration Rate (breaths per minute)", min_value=10, max_value=60, value=20)
GCS = st.number_input("Glasgow Coma Scale (GCS) Score", min_value=3, max_value=15, value=15)

# Calculate CART score
if st.button("Calculate CART Score"):
    cart_score = calculate_cart_score(age, systolic_bp, heart_rate, respiration_rate, GCS)
    st.success(f"The CART Score is: {cart_score}")
    if cart_score >= 3:
        st.warning("High risk of cardiac arrest. Consider immediate medical attention.")
    elif cart_score == 2:
        st.info("Moderate risk of cardiac arrest. Close monitoring is advised.")
    else:
        st.info("Low risk of cardiac arrest.")

# Footer
st.write("""
**Disclaimer:** This tool is for educational purposes only and should not be used as a substitute for professional medical advice.
""")
