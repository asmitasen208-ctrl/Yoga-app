import streamlit as st
import datetime

st.set_page_config(page_title="Wellness Pro", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Tabs (Audio & Guide removed)
tab1, tab2, tab3, tab4 = st.tabs(["Plan", "Tracker", "Daily Alarm", "Water"])

# Data
asana_data = {
    "Surya Namaskar": {"desc": "12 steps of sun salutation. Improves overall flexibility.", "img": "https://img.freepik.com/free-vector/yoga-poses-collection_23-2148530377.jpg"},
    "Tadasana": {"desc": "Mountain Pose: Stand tall, ground your feet, reach for the sky.", "img": "https://img.freepik.com/free-vector/woman-practicing-tadasana-yoga-pose_23-2148530375.jpg"},
    "Kapalbhati": {"desc": "Breathing exercise: Forceful exhalation to detoxify.", "img": "https://img.freepik.com/free-vector/man-practicing-breathing-exercise_23-2148530376.jpg"},
    "Bhujangasana": {"desc": "Cobra Pose: Lie on stomach, lift chest, arch back gently.", "img": "https://img.freepik.com/free-vector/woman-doing-cobra-yoga-pose_23-2148530378.jpg"},
    "Vajrasana": {"desc": "Thunderbolt Pose: Sit on heels, keep spine erect.", "img": "https://img.freepik.com/free-vector/person-sitting-vajrasana-yoga-pose_23-2148530379.jpg"}
}

with tab1:
    st.subheader("Personal Details")
    age = st.number_input("Age", 10, 100, 25)
    gender = st.radio("Gender", ["Male", "Female"])
    f = st.number_input("Height (ft)", 4, 7, 5)
    i = st.number_input("Height (inch)", 0, 11, 6)
    weight = st.number_input("Weight (kg)", 30, 200, 60)
    
    if st.button("Calculate & Get Plan"):
        height_m = ((f * 12) + i) * 0.0254
        bmi = weight / (height_m ** 2)
        status = "Underweight" if bmi < 18.5 else ("Normal" if bmi < 24.9 else "Overweight")
        st.success(f"BMI: {bmi:.1f} | Category: {status}")
        st.info("Your custom diet and exercise chart is ready in the Tracker tab!")

with tab2:
    st.subheader("Weekly Tracker")
    schedule = [("Day 1", "Surya Namaskar"), ("Day 2", "Tadasana"), ("Day 3", "Kapalbhati"), 
                ("Day 4", "REST"), ("Day 5", "Bhujangasana"), ("Day 6", "Vajrasana"), ("Day 7", "REST")]
    
    for day, name in schedule:
        with st.expander(f"{day}: {name}"):
            if st.checkbox(f"Done with {name}?", key=day):
                st.balloons()
            if name != "REST":
                st.image(asana_images[name]['img'], width=250)
                st.write(asana_data[name]['desc'])
                st.warning("⚠️ After this, take a 2-minute break!")
            else:
                st.write("Recovery Day. Stay hydrated!")

with tab3:
    st.subheader("⏰ Daily Alarm")
    # Time picker automatically shows AM/PM in standard browsers
    alarm = st.time_input("Set reminder time", datetime.time(8, 0))
    st.write(f"Reminder set for: **{alarm.strftime('%I:%M %p')}**")

with tab4:
    st.subheader("💧 Water Tracker")
    water = st.slider("Glasses of water today", 0, 12, 0)
    st.progress(water / 12)
