import streamlit as st
import datetime

st.set_page_config(page_title="Wellness Pro Guide", page_icon="🧘‍♀️")

# Asana Images Mapping
asana_images = {
    "Surya Namaskar": "https://img.freepik.com/free-vector/yoga-poses-collection_23-2148530377.jpg",
    "Tadasana": "https://img.freepik.com/free-vector/woman-practicing-tadasana-yoga-pose_23-2148530375.jpg",
    "Kapalbhati": "https://img.freepik.com/free-vector/man-practicing-breathing-exercise_23-2148530376.jpg",
    "Bhujangasana": "https://img.freepik.com/free-vector/woman-doing-cobra-yoga-pose_23-2148530378.jpg",
    "Vajrasana": "https://img.freepik.com/free-vector/person-sitting-vajrasana-yoga-pose_23-2148530379.jpg"
}

st.markdown("<h1 style='text-align: center;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Plan", "Tracker", "Daily Alarm", "Water", "Audio & Guide"])

# Data
weekly_plan = [
    ("Day 1", "Surya Namaskar"), ("Day 2", "Tadasana"), ("Day 3", "Kapalbhati"),
    ("Day 4", "REST"), ("Day 5", "Bhujangasana"), ("Day 6", "Vajrasana"), ("Day 7", "REST")
]

with tab1:
    st.subheader("Your Custom Plan")
    st.write("Generate your personalized fitness plan here.")

with tab2:
    st.subheader("Weekly Tracker")
    for day, asana in weekly_plan:
        st.checkbox(f"{day}: {asana}")
        if asana != "REST" and asana in asana_images:
            st.image(asana_images[asana], width=200)

with tab3:
    st.subheader("⏰ Daily Alarm")
    st.time_input("Set your yoga reminder", datetime.time(8, 0))

with tab4:
    st.subheader("💧 Water Tracker")
    water = st.slider("How many glasses have you had today?", 0, 12, 0)
    st.write(f"You have consumed {water * 250}ml of water.")
    st.progress(water / 12)

with tab5:
    st.subheader("Audio & Guide")
    st.write("Follow the written instructions for your daily asana.")
    # Audio player removed as requested
    
    # Logic to show instructions based on today's day
    today_index = datetime.datetime.now().weekday() # Simplified
    day_name, asana = weekly_plan[today_index]
    
    st.info(f"Today's Focus: {asana}")
    if asana == "REST":
        st.write("Enjoy your rest day and stay hydrated!")
    else:
        st.write(f"Guide for {asana}: Detailed step-by-step instructions will be provided here.")
