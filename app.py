import streamlit as st

# App Configuration
st.set_page_config(page_title="YogaForWeightGain", page_icon="🧘‍♀️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main-title {font-size: 30px; color: #FF4B4B; text-align: center; font-weight: bold;}
    .sub-text {font-size: 16px; color: #333333; text-align: center;}
    .card {background-color: #f9f9f9; padding: 20px; border-radius: 10px; margin-bottom: 15px;}
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-title">🧘‍♀️ Yoga & Wellness for Weight Gain</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Build strength, improve digestion, and gain healthy weight naturally.</p>', unsafe_allow_html=True)
st.divider()

# Sidebar Navigation
menu = st.sidebar.selectbox("Choose a Section", ["Home", "Asanas for Weight Gain", "Diet & Nutrition", "BMI Calculator"])

if menu == "Home":
    st.subheader("Welcome to Your Personal Yoga Journey!")
    
    st.write("""
    Unlike weight loss apps focused purely on calorie deficit, **Weight Gain Yoga** focuses on:
    * Improving overall digestion and nutrient absorption.
    * Building muscle mass through restorative and strength-building poses.
    * Reducing stress and balancing hormones to support healthy growth.
    """)

elif menu == "Asanas for Weight Gain":
    st.subheader("🌟 Recommended Asanas")
    
    asanas = {
        "1. Bhujangasana (Cobra Pose)": "Strengthens the spine, opens the chest, and improves metabolism and digestion.",
        "2. Sarvangasana (Shoulder Stand)": "Stimulates the thyroid gland which regulates metabolism and body weight.",
        "3. Pachimottanasana (Seated Forward Bend)": "Massages abdominal organs, improves appetite, and relieves stress.",
        "4. Vajrasana (Thunderbolt Pose)": "Best pose to practice right after meals to boost digestion and nutrient uptake."
    }
    
    for title, desc in asanas.items():
        with st.container():
            st.markdown(f"### {title}")
            st.write(desc)
            st.markdown("---")

elif menu == "Diet & Nutrition":
    st.subheader("🥗 Healthy Weight Gain Diet Tips")
    st.info("Yoga works best when paired with a nutrient-dense, calorie-surplus diet!")
    st.markdown("""
    * **Healthy Fats:** Include avocados, nuts, seeds, and ghee in your daily meals.
    * **Protein Rich Foods:** Paneer, lentils, tofu, and dairy products to support muscle building.
    * **Complex Carbs:** Sweet potatoes, brown rice, and oats for sustained energy.
    * **Hydration:** Drink plenty of water and herbal teas to keep your digestive tract healthy.
    """)

elif menu == "BMI Calculator":
    st.subheader("📊 Check Your Body Mass Index (BMI)")
    weight = st.number_input("Enter your weight (kg)", min_value=20.0, max_value=200.0, value=50.0)
    height = st.number_input("Enter your height (cm)", min_value=100.0, max_value=250.0, value=160.0)
    
    if st.button("Calculate BMI"):
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.success(f"Your BMI is: **{bmi:.2f}**")
        
        if bmi < 18.5:
            st.warning("You are in the underweight category. This app's yoga routines will help you gain healthy weight!")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal and healthy weight!")
        else:
            st.info("You are in the overweight category.")
