import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="Wellness Pro App", page_icon="🧘‍♀️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Tabs for Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Personalized Plan", "Water & Alarm", "Workout Timer", "Before & After", "AI Video & Audio"])

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
    st.subheader("💧 Water Tracker & ⏰ Custom Yoga Alarm")
    
    # Water Tracker
    if 'water' not in st.session_state: st.session_state.water = 0
    st.write(f"### Goal: 3 Liters | Progress: {st.session_state.water/1000:.1f} Liters")
    col_w1, col_w2 = st.columns(2)
    if col_w1.button("Add 250ml Water"): st.session_state.water += 250
    if col_w2.button("Reset Tracker"): st.session_state.water = 0
    st.progress(min(st.session_state.water / 3000, 1.0))
    
    st.divider()
    
    # Alarm & Schedule Section
    st.subheader("🔔 Set Daily Yoga Alarm & Rest Days")
    alarm_time = st.time_input("Select Daily Notification/Alarm Time")
    rest_days = st.multiselect("Select Days to Rest (No Yoga):", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], default=["Sunday"])
    if st.button("Save Schedule & Alarm"):
        st.success(f"Alarm set for {alarm_time.strftime('%H:%M')} daily! Rest days scheduled: {', '.join(rest_days)}.")

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
    st.subheader("📸 Side-by-Side Before & After Progress")
    st.write("First day practice photo (Before) aur 1 mahine baad ki photo (After) yahan upload karke apni progress compare karein:")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown("#### 1️⃣ First Day (Before)")
        before_img = st.file_uploader("Upload First Day Photo", type=['jpg', 'png', 'jpeg'], key="b")
        if before_img: st.image(before_img, caption="Day 1", use_column_width=True)
    with col_p2:
        st.markdown("#### 2️⃣ After 1 Month (Progress)")
        after_img = st.file_uploader("Upload After 1 Month Photo", type=['jpg', 'png', 'jpeg'], key="a")
        if after_img: st.image(after_img, caption="After 1 Month", use_column_width=True)
        
    if before_img and after_img:
        st.balloons()
        st.success("Amazing transformation progress! Keep it up!")

with tab5:
    st.subheader("🎥 AI Video & Audio Guided Yoga")
    st.markdown("### 🌊 Calm Ocean & Relaxation Music")
    st.audio("https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf756.mp3?filename=gentle-waves-ambient-111242.mp3", format="audio/mp3")
    
    st.markdown("---")
    selected_asan = st.selectbox("Choose Asan to Learn:", ["Bhujangasana (Cobra Pose)", "Vajrasana (Thunderbolt Pose)", "Kapalbhati Pranayama"])
    
    if selected_asan == "Bhujangasana (Cobra Pose)":
        st.image("https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600", caption="Bhujangasana Guide")
        st.info("🗣️ **AI Voice Guide:** Pait ke bal let jayein, dono hath shoulders ke paas rakhein, aur saans lete huye upper body ko dheere-dheere upar uthayein.")
    elif selected_asan == "Vajrasana (Thunderbolt Pose)":
        st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=600", caption="Vajrasana Guide")
        st.info("🗣️ **AI Voice Guide:** Ghutno par baith jayein, hips ko heels par tikayein, aur peeth seedhi karke lambi saans lein.")
    else:
        st.image("https://images.unsplash.com/photo-1599447421416-3414500d18a5?w=600", caption="Kapalbhati Guide")
        st.info("🗣️ **AI Voice Guide:** Palthi maarkar comfortable baithein, ankhein band karein, aur pet se saans ko forceful tarike se bahar fekein.")

st.sidebar.info("Stay consistent, stay healthy! 🌿")
