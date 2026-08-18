import streamlit as st
import time

# App Configuration
st.set_page_config(page_title="Wellness Pro App", page_icon="🧘‍♀️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🧘‍♀️ Wellness Pro Guide</h1>", unsafe_allow_html=True)

# Tabs for Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Personalized Plan", "Water Tracker", "Workout Timer", "Progress Log", "AI Video & Audio Guide"])

with tab1:
    st.subheader("Get Your Custom Plan")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", 10, 100, 25)
    with col2:
        weight = st.number_input("Weight (kg)", 20.0, 200.0, 50.0)
        height = st.number_input("Height (cm)", 100.0, 250.0, 160.0)

    if st.button("✨ Generate Plan"):
        bmi = weight / ((height/100) ** 2)
        st.write(f"### Your BMI: {bmi:.1f}")
        st.success("Follow these daily for a healthy life!")

with tab2:
    st.subheader("💧 Daily Water Tracker")
    if 'water' not in st.session_state: st.session_state.water = 0
    st.write(f"### Goal: 3 Liters | Progress: {st.session_state.water/1000:.1f} Liters")
    
    col_w1, col_w2 = st.columns(2)
    if col_w1.button("Add 250ml Water"): st.session_state.water += 250
    if col_w2.button("Reset Tracker"): st.session_state.water = 0
    st.progress(min(st.session_state.water / 3000, 1.0))

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
    st.subheader("📸 Before & After Progress")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        before_img = st.file_uploader("Upload 'Before' Photo", type=['jpg', 'png', 'jpeg'], key="b")
        if before_img: st.image(before_img, caption="Before", use_column_width=True)
    with col_p2:
        after_img = st.file_uploader("Upload 'After' Photo", type=['jpg', 'png', 'jpeg'], key="a")
        if after_img: st.image(after_img, caption="After", use_column_width=True)
    if before_img and after_img:
        st.balloons()
        st.success("Great job on your fitness journey!")

with tab5:
    st.subheader("🎥 AI Video & Audio Guided Yoga")
    st.write("Yahan aap asan dekh kar follow kar sakte hain aur background music play kar sakte hain:")
    
    # Background Music (Royalty-free relaxing flute/meditation music)
    st.markdown("### 🎵 Relaxing Background Music")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
    
    st.markdown("---")
    st.markdown("### 🧘‍♂️ Asan Demonstration & Voice Steps")
    
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
