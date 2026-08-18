import streamlit as st
import datetime

# App Configuration
st.set_page_config(page_title="Wellness Pro App", page_icon="🧘‍♀️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Plan", "Tracker", "Daily Alarm", "Progress", "Audio & Guide"])

# Logic for dynamic Asanas based on Day
def get_daily_asan(day_num, bmi_cat):
    routines = {
        "Underweight": ["Bhujangasana", "Vajrasana", "Tadasana", "REST", "Dhanurasana", "Surya Namaskar", "REST"],
        "Normal": ["Surya Namaskar", "Tadasana", "Kapalbhati", "REST", "Bhujangasana", "Vajrasana", "REST"],
        "Overweight": ["Kapalbhati", "Dhanurasana", "Surya Namaskar", "REST", "Bhujangasana", "Tadasana", "REST"]
    }
    return routines.get(bmi_cat, ["Stretch"]*7)[(day_num-1) % 7]

with tab1:
    st.subheader("Your Custom Plan")
    gender = st.selectbox("Gender", ["Female", "Male"])
    col1, col2 = st.columns(2)
    weight = col1.number_input("Weight (kg)", 20.0, 200.0, 50.0)
    height = col2.number_input("Height (cm)", 100.0, 250.0, 160.0)
    
    if st.button("Generate Plan"):
        bmi = weight / ((height/100) ** 2)
        cat = "Underweight" if bmi < 18.5 else ("Normal" if bmi < 24.9 else "Overweight")
        st.session_state.bmi_cat = cat
        st.success(f"Category: {cat}")

with tab2:
    st.subheader("Weekly Tracker")
    cat = st.session_state.get('bmi_cat', 'Normal')
    for i in range(1, 8):
        asan = get_daily_asan(i, cat)
        if st.checkbox(f"Day {i}: {asan}", key=f"day{i}"):
            st.session_state.last_day = i

with tab3:
    st.subheader("⏰ Set Yoga Alarm")
    alarm_time = st.time_input("Set your yoga time", datetime.time(8, 0))
    st.info(f"Notification alert is set for: {alarm_time.strftime('%I:%M %p')}")

with tab4:
    st.subheader("Progress & Comparison")
    before = st.file_uploader("Upload Day 1 Photo", type=['jpg', 'png'], key="b")
    # Only show 'After' if Day 30 is reached (simplified check)
    if st.session_state.get('last_day', 0) >= 1: # You can change this to 30 for production
        after = st.file_uploader("Upload Day 30 Photo", type=['jpg', 'png'], key="a")
        if before and after:
            c1, c2 = st.columns(2)
            c1.image(before, "Day 1")
            c2.image(after, "Day 30")
    else:
        st.warning("After 30 days of tracking, the comparison option will unlock.")

with tab5:
    st.subheader("Audio & Guide")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Placeholder for Ocean Sound
    
    cat = st.session_state.get('bmi_cat', 'Normal')
    today_day = st.session_state.get('last_day', 1)
    current_asan = get_daily_asan(today_day, cat)
    
    st.markdown(f"### Today's Focus: {current_asan}")
    if current_asan == "REST":
        st.info("Today is your recovery day. Relax!")
    else:
        st.write(f"Guide for {current_asan}: Follow the voice instruction.")
        st.info("🗣️ AI Voice: Focus on your breathing and posture.")
