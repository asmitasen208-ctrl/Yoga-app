import streamlit as st
import datetime

st.set_page_config(page_title="Wellness Pro", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Session State for Progress
if 'completed_days' not in st.session_state:
    st.session_state.completed_days = 0

tab1, tab2, tab3, tab4 = st.tabs(["Plan", "Tracker", "Daily Alarm", "Water"])

asana_data = {
    "Surya Namaskar": {"desc": "12 steps of sun salutation. Improves overall flexibility.", "img": "https://img.freepik.com/free-vector/yoga-poses-collection_23-2148530377.jpg"},
    "Tadasana": {"desc": "Mountain Pose: Stand tall, ground your feet, reach for the sky.", "img": "https://img.freepik.com/free-vector/woman-practicing-tadasana-yoga-pose_23-2148530375.jpg"},
    "Kapalbhati": {"desc": "Breathing exercise: Forceful exhalation to detoxify.", "img": "https://img.freepik.com/free-vector/man-practicing-breathing-exercise_23-2148530376.jpg"},
    "Bhujangasana": {"desc": "Cobra Pose: Lie on stomach, lift chest, arch back gently.", "img": "https://img.freepik.com/free-vector/woman-doing-cobra-yoga-pose_23-2148530378.jpg"},
    "Vajrasana": {"desc": "Thunderbolt Pose: Sit on heels, keep spine erect.", "img": "https://img.freepik.com/free-vector/person-sitting-vajrasana-yoga-pose_23-2148530379.jpg"}
}

with tab1:
    st.subheader("Transformation Tracker")
    st.image(st.file_uploader("Upload your 'Before' Photo", type=['jpg', 'png']), caption="Your Starting Point")
    
    if st.session_state.completed_days >= 30:
        st.image(st.file_uploader("Upload your 'After' Photo (Congrats!)", type=['jpg', 'png']), caption="Your Result")
    else:
        st.info(f"Complete 30 days of yoga to unlock the 'After' photo upload. Current streak: {st.session_state.completed_days}/30")

with tab2:
    st.subheader("Weekly Exercise Tracker")
    schedule = [("Day 1", "Surya Namaskar"), ("Day 2", "Tadasana"), ("Day 3", "Kapalbhati"), 
                ("Day 4", "REST"), ("Day 5", "Bhujangasana"), ("Day 6", "Vajrasana"), ("Day 7", "REST")]
    
    for day, name in schedule:
        with st.expander(f"{day}: {name}"):
            if st.checkbox(f"Completed {name}?", key=f"done_{day}"):
                st.session_state.completed_days += 1
                st.success("Great! Don't forget your 2-minute break.")
                st.balloons()
            
            if name != "REST":
                st.image(asana_data[name]['img'], width=250)
                st.write(f"**Guide:** {asana_data[name]['desc']}")
                st.warning("⚠️ Mandatory: Take a 2-minute break after this!")

with tab3:
    st.subheader("⏰ Set Yoga Reminder")
    # Using time_input which handles AM/PM based on system locale
    alarm = st.time_input("Choose your preferred time", datetime.time(8, 0))
    st.write(f"Notification set for: **{alarm.strftime('%I:%M %p')}**")

with tab4:
    st.subheader("💧 Water Tracker")
    water = st.slider("Glasses of water today", 0, 12, 0)
    st.progress(water / 12)
