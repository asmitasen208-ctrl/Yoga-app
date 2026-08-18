import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="Wellness Pro App", page_icon="🧘‍♀️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Tabs for Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Personalized Plan", "Schedule & Tracker", "Workout Timer", "Progress & Comparison", "AI Video & Audio"])

with tab1:
    st.subheader("Get Your Custom Plan & Diet Chart")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", 10, 100, 25)
    with col2:
        weight = st.number_input("Weight (kg)", 20.0, 200.0, 50.0)
        height = st.number_input("Height (cm)", 100.0, 250.0, 160.0)

    if st.button("✨ Generate Complete Plan"):
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        min_ideal_weight = 18.5 * (height_m ** 2)
        max_ideal_weight = 24.9 * (height_m ** 2)
        
        st.divider()
        st.subheader(f"📊 Your BMI: {bmi:.1f}")

        if bmi < 18.5:
            diff = min_ideal_weight - weight
            st.warning(f"You are Underweight by approximately **{diff:.1f} kg**.")
            st.markdown("### 🍽️ Surplus Diet Chart")
            st.markdown("""
            | Meal Time | What to Eat |
            | :--- | :--- |
            | **Breakfast** | Stuffed parathas with butter/curd, full-cream milk, and dry fruits. |
            | **Lunch** | Multi-grain chapati, heavy dal/paneer curry, rice, and a bowl of curd. |
            | **Dinner** | Nutritious khichdi or paneer sabzi with roti, followed by warm milk with ghee. |
            """)
        elif 18.5 <= bmi < 24.9:
            st.success("Congratulations! You have a Normal and Healthy weight.")
            st.markdown("### 🍽️ Balanced Diet Chart")
            st.markdown("""
            | Meal Time | What to Eat |
            | :--- | :--- |
            | **Breakfast** | Oats/Poha, sprouts, or eggs with fresh fruit juice. |
            | **Lunch** | Balanced portion of chapati, seasonal vegetables, dal, and fresh salad. |
            | **Dinner** | Light dinner including vegetable soup or light dal-roti. |
            """)
        else:
            diff = weight - max_ideal_weight
            st.info(f"You are Overweight by approximately **{diff:.1f} kg**.")
            st.markdown("### 🍽️ Fat-Loss Diet Chart")
            st.markdown("""
            | Meal Time | What to Eat |
            | :--- | :--- |
            | **Breakfast** | Warm lemon-honey water, green tea, and sprouted moong or egg whites. |
            | **Lunch** | Large bowl of salad, 1-2 thin chapati, dal, and green leafy vegetables. |
            | **Dinner** | Light vegetable soup or boiled/roasted veggies (finish before 8 PM). |
            """)

with tab2:
    st.subheader("📅 Weekly Yoga Schedule & Daily Tracker")
    st.write("Follow this routine day-by-day. Check the box once you complete your daily exercise!")
    
    # Initialize tracker state
    if 'days_tracked' not in st.session_state:
        st.session_state.days_tracked = 0

    schedule = [
        ("Day 1", "Surya Namaskar & Tadasana", False),
        ("Day 2", "Bhujangasana & Vajrasana", False),
        ("Day 3", "REST DAY (No Yoga)", True),
        ("Day 4", "Kapalbhati Pranayama & Dhanurasana", False),
        ("Day 5", "Surya Namaskar & Core Stretching", False),
        ("Day 6", "REST DAY (No Yoga)", True),
        ("Day 7", "Light Meditation & Breathing Exercises", False),
    ]

    completed_count = 0
    for day, asans, is_rest in schedule:
        st.markdown(f"**{day}:** {asans}")
        if not is_rest:
            key_name = f"chk_{day}"
            if st.checkbox(f"Mark {day} Exercise Done", key=key_name):
                completed_count += 1
        else:
            st.info("🛋️ Relax and recover today!")
        st.markdown("---")
    
    # Store total completed workout days
    st.session_state.days_tracked = completed_count
    st.write(f"### Total Workout Days Completed: {st.session_state.days_tracked} / 5")

with tab3:
    st.subheader("⏱️ Daily Workout Timer")
    duration = st.slider("Select Duration (minutes)", 5, 60, 15)
    if st.button("Start Timer"):
        with st.empty():
            for s in range(duration * 60, 0, -1):
                mins, secs = divmod(s, 60)
                st.markdown(f"<h2 style='text-align: center;'>Remaining: {mins:02d}:{secs:02d}</h2>", unsafe_allow_html=True)
                time.sleep(1)
            st.success("Workout Complete!")

with tab4:
    st.subheader("📸 Progress & Before/After Comparison")
    
    # Always allow uploading 'Before' photo on Day 1
    st.markdown("#### 1️⃣ First Day Photo (Before)")
    before_img = st.file_uploader("Upload your Day 1 photo", type=['jpg', 'png', 'jpeg'], key="b_img")
    if before_img:
        st.image(before_img, caption="Day 1 (Before)", width=300)
    
    st.divider()
    
    # Check if 30 days/workouts are completed to unlock After photo
    if st.session_state.get('days_tracked', 0) >= 5: # Setting threshold (can be adjusted to 30 when using real dates)
        st.success("🎉 Congratulations! You have unlocked your 30-Day Progress Comparison!")
        st.markdown("#### 2️⃣ After 30 Days Photo (After)")
        after_img = st.file_uploader("Upload your After 30 Days photo", type=['jpg', 'png', 'jpeg'], key="a_img")
        
        if before_img and after_img:
            st.markdown("### 🔄 Side-by-Side Comparison")
            col_c1, col_c2 = st.columns(2)
            with col_c1:
                st.image(before_img, caption="Before", use_column_width=True)
            with col_c2:
                st.image(after_img, caption="After 30 Days", use_column_width=True)
            st.balloons()
            st.success("Amazing transformation! Look at your incredible progress.")
    else:
        st.info("🔒 **After 30 Days Photo is locked!** Complete at least 5 workout tracking checkboxes in the 'Schedule & Tracker' tab to unlock your comparison view.")

with tab5:
    st.subheader("🎥 AI Video & Audio Guided Yoga")
    st.markdown("### 🌊 Calm Ocean & Relaxation Music")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
    
    st.markdown("---")
    selected_asan = st.selectbox("Choose Asan to Learn:", ["Bhujangasana (Cobra Pose)", "Vajrasana (Thunderbolt Pose)", "Kapalbhati Pranayama"])
    
    if selected_asan == "Bhujangasana (Cobra Pose)":
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600", caption="Bhujangasana Guide")
        st.info("🗣️ **AI Voice Guide:** Lie down on your stomach, place both hands near your shoulders, and inhale while lifting your upper body gently.")
    elif selected_asan == "Vajrasana (Thunderbolt Pose)":
        st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600", caption="Vajrasana Guide")
        st.info("🗣️ **AI Voice Guide:** Sit on your knees, rest your hips on your heels, keep your spine straight, and take deep breaths.")
    else:
        st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?w=600", caption="Kapalbhati Guide")
        st.info("🗣️ **AI Voice Guide:** Sit comfortably with cross legs, close your eyes, and forcefully exhale air through your stomach.")

st.sidebar.info("Stay consistent, stay healthy! 🌿")

