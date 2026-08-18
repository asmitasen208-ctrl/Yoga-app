import streamlit as st

# App Configuration
st.set_page_config(page_title="Yoga Personal Guide", page_icon="🧘‍♀️", layout="centered")

st.markdown('<h1 style="text-align: center; color: #FF4B4B;">🧘‍♀️ Personalized Yoga & Diet Guide</h1>', unsafe_allow_html=True)
st.write("Enter your details below to get your personalized health and wellness plan:")

# User Inputs
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", min_value=10, max_value=100, value=25)
    with col2:
        weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=50.0)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=160.0)

if st.button("Generate My Plan"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    st.divider()
    st.subheader(f"Result: Your BMI is {bmi:.1f}")

    if bmi < 18.5:
        st.warning("You are in the Underweight category.")
        st.markdown("### 🌟 Yoga for Weight Gain")
        st.write("- **Bhujangasana (Cobra Pose):** Helps improve metabolism and strengthens the spine.")
        st.write("- **Vajrasana (Thunderbolt Pose):** Best practiced after meals to boost digestion.")
        st.markdown("### 🥗 Recommended Diet")
        st.write("- Include healthy fats like ghee, nuts, and seeds.")
        st.write("- Eat protein-rich foods like paneer, lentils, and dairy products.")

    elif 18.5 <= bmi < 24.9:
        st.success("You have a Normal and Healthy weight!")
        st.markdown("### 🌟 Yoga for Maintenance")
        st.write("- **Surya Namaskar (Sun Salutation):** Great for overall body flexibility and fitness.")
        st.write("- **Tadasana (Mountain Pose):** Excellent for posture and stability.")
        st.markdown("### 🥗 Recommended Diet")
        st.write("- Maintain a balanced diet with fresh fruits, vegetables, and whole grains.")

    else:
        st.info("You are in the Overweight category.")
        st.markdown("### 🌟 Yoga for Weight Loss")
        st.write("- **Kapalbhati Pranayama:** Boosts metabolism and aids in fat burning.")
        st.write("- **Dhanurasana (Bow Pose):** Massages abdominal organs and helps reduce belly fat.")
        st.markdown("### 🥗 Recommended Diet")
        st.write("- Increase intake of high-fiber foods, salads, and green vegetables.")
        st.write("- Avoid processed sugars, junk food, and excessive oils.")

st.sidebar.info("This application is designed for general wellness guidance. Consult a professional before starting any new fitness routine.")
