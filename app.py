import streamlit as st

# Page Configuration
st.set_page_config(page_title="Yoga App", layout="centered")

# Initialize Session State for Flow Control
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'data' not in st.session_state:
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

def prev_step():
    if st.session_state.step > 1:
        st.session_state.step -= 1
        st.rerun()

# --- SLIDE 1: Welcome (No Image, Styled Text) ---
if st.session_state.step == 1:
    st.markdown("<h1 style='text-align: center; margin-top: 60px; color: #2C3E50;'>Yoga For Weight Loss</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #16A085; font-weight: bold;'>Yoga for better and healthy life</h3>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    if st.button("Get Started", use_container_width=True):
        next_step()

# --- SLIDE 2: Move Gently (Multiple Checkboxes) ---
elif st.session_state.step == 2:
    st.markdown("<h2 style='text-align: center;'>Move Gently, Improve Rapidly</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("What would you like to focus on? (Select as many as you want)")
    
    options = ["Improve Health", "Sleep Better", "Clear Mind", "Stay Young"]
    selected_focus = []
    for opt in options:
        if st.checkbox(opt, key=f"focus_{opt}"):
            selected_focus.append(opt)
            
    st.session_state.data['focus'] = selected_focus
    
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 3: Additional Preferences ---
elif st.session_state.step == 3:
    st.markdown("<h2 style='text-align: center;'>Tell us a bit more</h2>", unsafe_allow_html=True)
    st.write("---")
    st.session_state.data['pace'] = st.radio("Preferred workout pace:", ["Gentle & Relaxing", "Moderate", "Dynamic & Fast"])
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 4: Main Goal ---
elif st.session_state.step == 4:
    st.markdown("<h2 style='text-align: center;'>What's your main goal?</h2>", unsafe_allow_html=True)
    goals = ["Lose Weight", "Keep Fit", "Relax & Unwind", "Flexibility", "Recovery"]
    st.session_state.data['goal'] = st.radio("Select your main goal:", goals)
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 5: Present Shape ---
elif st.session_state.step == 5:
    st.markdown("<h2 style='text-align: center;'>What's your current body shape?</h2>", unsafe_allow_html=True)
    st.session_state.data['body_fat'] = st.slider("Your estimated body fat (%)", 15, 40, 30)
    st.info(f"Estimated Body Fat: **{st.session_state.data['body_fat']}%**")
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 6: Help Screen ---
elif st.session_state.step == 6:
    st.markdown("<h2 style='text-align: center;'>We're here to help people like you!</h2>", unsafe_allow_html=True)
    st.success("83% of our users rated our customized yoga programs as easy to follow and have achieved excellent results with practice.")
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 7: Gender ---
elif st.session_state.step == 7:
    st.markdown("<h2 style='text-align: center;'>What's your gender?</h2>", unsafe_allow_html=True)
    st.session_state.data['gender'] = st.radio("Select gender:", ["Male", "Female", "Prefer not to say"])
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 8: Age ---
elif st.session_state.step == 8:
    st.markdown("<h2 style='text-align: center;'>How old are you?</h2>", unsafe_allow_html=True)
    st.session_state.data['age'] = st.number_input("Enter your age", 10, 100, 30)
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 9: Height ---
elif st.session_state.step == 9:
    st.markdown("<h2 style='text-align: center;'>What's your height?</h2>", unsafe_allow_html=True)
    height = st.slider("Height (cm)", 100, 220, 165)
    st.session_state.data['height'] = height
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 10: Current Weight & BMI ---
elif st.session_state.step == 10:
    st.markdown("<h2 style='text-align: center;'>What's your current weight?</h2>", unsafe_allow_html=True)
    weight_kg = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    st.session_state.data['current_weight'] = weight_kg
    
    if 'height' in st.session_state.data:
        height_m = st.session_state.data['height'] / 100
        bmi = weight_kg / (height_m ** 2)
        st.session_state.data['bmi'] = bmi
        
        if bmi < 18.5:
            bmi_status = "Underweight"
            msg = "You may need to focus on gaining healthy mass!"
        elif 18.5 <= bmi < 25:
            bmi_status = "Healthy"
            msg = "You are in good shape!"
        elif 25 <= bmi < 30:
            bmi_status = "Overweight"
            msg = "You may need to do more workouts to be better and healthier!"
        else:
            bmi_status = "Obesity"
            msg = "You may need to do more workouts to be better and healthier!"
            
        st.warning(f"**Your BMI: {bmi:.1f} ({bmi_status})**\n\n{msg}")
        
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 11: Target Weight ---
elif st.session_state.step == 11:
    st.markdown("<h2 style='text-align: center;'>Do you have a target weight?</h2>", unsafe_allow_html=True)
    target_weight = st.slider("Target Weight (kg)", 30.0, 150.0, 55.0)
    st.session_state.data['target_weight'] = target_weight
    
    if target_weight < 45.0:
        st.error("⚠️ **Attention!** It seems that your target BMI is too low, which might cause some health problems...")
        
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 12: Assessment & Prediction Date ---
elif st.session_state.step == 12:
    st.markdown("<h2 style='text-align: center;'>Your goal is closer than expected!</h2>", unsafe_allow_html=True)
    target_wt = st.session_state.data.get('target_weight', 55.0)
    st.markdown(f"<h3 style='text-align: center; color: purple;'>{target_wt} kg by Oct 12</h3>", unsafe_allow_html=True)
    st.info("🔥 **14 Days Early!** Your personalized plan will put you on track to reach your goal earlier—exciting potential!")
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 13: Yoga Experience ---
elif st.session_state.step == 13:
    st.markdown("<h2 style='text-align: center;'>Have you practiced yoga before?</h2>", unsafe_allow_html=True)
    experience_options = [
        "Never practiced before (I'd like to start here)",
        "Practiced several times (I can do some gentle poses)",
        "I'm experienced (I can perform advanced poses)"
    ]
    st.session_state.data['experience'] = st.radio("Select your level:", experience_options)
    if st.button("Next", use_container_width=True):
        next_step()

# --- SLIDE 14: Training Schedule & Day 1 Plan (No Images, Rich Benefits List) ---
elif st.session_state.step == 14:
    st.markdown("<h2 style='text-align: center;'>With your personalized Plan</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>You'll be your target weight by Sep 14</h3>", unsafe_allow_html=True)
    st.write("86% of users in a similar situation to you have lost weight with a personalized 30-day yoga plan.")
    
    st.write("---")
    st.subheader("Training Schedule (September)")
    
    selected_day = st.selectbox("Select date to view routine:", [18, 19, 20, 21, 22, 23, 24], index=0)
    
    if selected_day == 18:
        st.markdown("### 🧘 Day 1 Workout Routine")
        
        exercises = [
            {"name": "1. Seated Cat Cow", "duration": "00:50", "benefit": "Improves spine flexibility, posture, and relieves back tension."},
            {"name": "2. Crescent Low Lunge Left", "duration": "00:40", "benefit": "Stretches hips, thighs, and groin while building lower body stability."},
            {"name": "3. Half Locust Pose", "duration": "00:40", "benefit": "Strengthens back muscles, glutes, and the back of arms and legs."},
            {"name": "4. Downward Facing Dog With Bent Knees", "duration": "00:50", "benefit": "Energizes the body, stretches shoulders, hamstrings, and calves."},
            {"name": "5. Crescent Low Lunge Right", "duration": "00:40", "benefit": "Balances right-side body strength and improves hip mobility."},
            {"name": "6. Bird Dog", "duration": "00:50", "benefit": "Improves core stability, coordination, and supports lower back health."},
            {"name": "7. Sphinx Pose", "duration": "00:50", "benefit": "Gentle backbend that strengthens the spine and opens the chest."},
            {"name": "8. Child's Pose", "duration": "00:50", "benefit": "Deep relaxation pose that calms the central nervous system and relieves fatigue."},
            {"name": "9. Relaxation Lying Pose (Savasana)", "duration": "01:00", "benefit": "Final resting pose to integrate practice benefits and reduce stress."}
        ]
        
        for ex in exercises:
            st.markdown(f"#### **{ex['name']}**")
            st.text(f"⏱️ Duration: {ex['duration']}")
            st.markdown(f"💡 **Benefits:** {ex['benefit']}")
            st.divider()
            
        if st.button("START WORKOUT SESSION", use_container_width=True):
            st.balloons()
            st.success("Session Started Successfully! Enjoy your practice.")
    else:
        st.info(f"Routine for September {selected_day} will unlock sequentially. Please check Day 1 (18th).")

# Back button utility at the bottom
if st.session_state.step > 1:
    st.write("---")
    if st.button("⬅ Back"):
        prev_step()
