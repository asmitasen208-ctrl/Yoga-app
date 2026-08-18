import streamlit as st
import datetime

st.set_page_config(page_title="Wellness Pro", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Plan", "Tracker", "Daily Alarm", "Water"])

# Asana Details
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
    
    if st.button("Generate My Plan"):
        height_m = ((f * 12) + i) * 0.0254
        bmi = weight / (height_m ** 2)
        
        # BMI Interpretation
        if bmi < 18.5:
            msg = f"You are Underweight (BMI: {bmi:.1f}). Focus on protein-rich diet and strength-building yoga."
        elif 18.5 <= bmi < 25:
            msg = f"You have Normal weight (BMI: {bmi:.1f}). Maintain your routine for healthy living."
        else:
            msg = f"You are Overweight (BMI: {bmi:.1f}). Focus on cardio-heavy yoga and calorie-controlled diet."
        
        st.success(msg)
        st.info("Check the 'Tracker' tab to see your daily exercise schedule.")

with tab2:
    st.subheader("Weekly Exercise Tracker")
    schedule = [("Day 1", "Surya Namaskar"), ("Day 2", "Tadasana"), ("Day 3", "Kapalbhati"), 
                ("Day 4", "REST"), ("Day 5", "Bhujangasana"), ("Day 6", "Vajrasana"), ("Day 7", "REST")]
    
    for day, name in schedule:
        with st.expander(f"{day}: {name}"):
            if st.checkbox(f"Completed {name}?", key=day):
                st.balloons()
            if name != "REST":
                st.image(asana_data[name]['img'], width=250)
                st.write(f"**Guide:** {asana_data[name]['desc']}")
                st.warning("⚠️ After finishing, take a mandatory 2-minute break!")
            else:
                st.write("Recovery & Rest Day. Keep yourself relaxed and stay hydrated!")

with tab3:
    st.subheader("⏰ Daily Yoga Alarm")
    alarm = st.time_input("Set your yoga reminder time", datetime.time(8, 0))
    st.write(f"Your daily reminder is set for: **{alarm.strftime('%I:%M %p')}**")

with tab4:
    st.subheader("💧 Water Tracker")
    water = st.slider("How many glasses have you had today?", 0, 12, 0)
    st.progress(water / 12)
    st.write(f"You have consumed {water * 250}ml of water.")
