import streamlit as st

# App Configuration
st.set_page_config(page_title="Personalized Yoga & Diet Guide", page_icon="🧘‍♀️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧘‍♀️ Personalized Yoga & Diet Guide</h1>", unsafe_allow_html=True)
st.write("Enter your details below to get your custom health, meal plan, and yoga guide:")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    age = st.number_input("Age", min_value=10, max_value=100, value=25)
with col2:
    weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=50.0)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=160.0)

if st.button("✨ Generate My Complete Plan"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    min_ideal_weight = 18.5 * (height_m ** 2)
    max_ideal_weight = 24.9 * (height_m ** 2)
    
    st.divider()
    st.subheader(f"📊 Your BMI Result: {bmi:.1f}")

    if bmi < 18.5:
        diff = min_ideal_weight - weight
        st.warning(f"You are Underweight by approximately **{diff:.1f} kg**.")
        
        st.markdown("### ⏰ Yoga Timing")
        st.info("Best time: Early morning on an empty stomach, or evening (4 hours after a heavy meal).")
        
        st.markdown("### 🌟 Recommended Yoga Asanas")
        
        col_y1, col_y2 = st.columns(2)
        with col_y1:
            st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400", caption="Bhujangasana (Cobra Pose)")
            st.write("**Bhujangasana:** Improves metabolism and strengthens the spine.")
        with col_y2:
            st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400", caption="Vajrasana (Thunderbolt Pose)")
            st.write("**Vajrasana:** Practice for 5-10 mins after meals to boost digestion.")

        st.markdown("### 🍽️ Daily Meal Plan (Surplus Diet Chart)")
        st.markdown("""
        | Meal Time | What to Eat |
        | :--- | :--- |
        | **Breakfast** | Stuffed parathas with butter/curd, full-cream milk, and a handful of dry fruits. |
        | **Lunch** | Multi-grain chapati, heavy dal/paneer curry, rice, and a bowl of curd. |
        | **Dinner** | Nutritious khichdi or paneer sabzi with roti, followed by warm milk with ghee. |
        """)

    elif 18.5 <= bmi < 24.9:
        st.success("Congratulations! You have a Normal and Healthy weight.")
        
        st.markdown("### ⏰ Yoga Timing")
        st.info("Best time: Early morning to maintain daily flexibility and freshness.")
        
        st.markdown("### 🌟 Recommended Yoga Asanas")
        
        col_y1, col_y2 = st.columns(2)
        with col_y1:
            st.image("https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=400", caption="Surya Namaskar")
            st.write("**Surya Namaskar:** Great for overall body stamina and flexibility.")
        with col_y2:
            st.image("https://images.unsplash.com/photo-1575052814086-f385e2e2ad1b?w=400", caption="Tadasana (Mountain Pose)")
            st.write("**Tadasana:** Excellent for posture and body balance.")

        st.markdown("### 🍽️ Daily Meal Plan (Balanced Diet Chart)")
        st.markdown("""
        | Meal Time | What to Eat |
        | :--- | :--- |
        | **Breakfast** | Oats/Poha, sprouts, or eggs with fresh fruit juice. |
        | **Lunch** | Balanced portion of chapati, seasonal vegetables, dal, and fresh salad. |
        | **Dinner** | Light dinner including vegetable soup or light dal-roti (eat 2 hours before sleep). |
        """)

    else:
        diff = weight - max_ideal_weight
        st.info(f"You are Overweight by approximately **{diff:.1f} kg**.")
        
        st.markdown("### ⏰ Yoga Timing")
        st.info("Best time: Morning empty stomach to activate metabolism and burn fat.")
        
        st.markdown("### 🌟 Recommended Yoga Asanas")
        
        col_y1, col_y2 = st.columns(2)
        with col_y1:
            st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?w=400", caption="Pranayama / Breathing")
            st.write("**Kapalbhati:** 10-15 minutes daily to boost metabolism and burn belly fat.")
        with col_y2:
            st.image("https://images.unsplash.com/photo-1518611012118-696072aa579a?w=400", caption="Dhanurasana (Bow Pose)")
            st.write("**Dhanurasana:** Stretches abdominal organs and reduces fat.")

        st.markdown("### 🍽️ Daily Meal Plan (Fat-Loss Diet Chart)")
        st.markdown("""
        | Meal Time | What to Eat |
        | :--- | :--- |
        | **Breakfast** | Warm lemon-honey water, green tea, and sprouted moong or egg whites. |
        | **Lunch** | Large bowl of salad, 1-2 thin chapati, dal, and green leafy vegetables. |
        | **Dinner** | Light vegetable soup or boiled/roasted veggies (finish eating before 8 PM). |
        """)

st.sidebar.markdown("### About App")
st.sidebar.info("This app provides clean schedules, visual yoga guides, and diet charts tailored to your BMI.")
