import streamlit as st

# App Configuration
st.set_page_config(page_title="Personalized Yoga & Diet Guide", page_icon="🧘‍♀️", layout="centered")

# Custom CSS for Beautiful UI
st.markdown("""
    <style>
    .main-title {
        font-size: 26px;
        color: #FF4B4B;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-text {
        font-size: 14px;
        color: #555555;
        text-align: center;
        margin-bottom: 20px;
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 5px solid #FF4B4B;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e03e3e;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="main-title">🧘‍♀️ Personalized Yoga & Diet Guide</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Enter your details to get your custom health & meal plan</p>', unsafe_allow_html=True)

# User Inputs inside a clean container
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        age = st.number_input("Age", min_value=10, max_value=100, value=25)
    with col2:
        weight = st.number_input("Weight (kg)", min_value=20.0, max_value=200.0, value=50.0)
        height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=160.0)

st.write("")
if st.button("✨ Generate My Complete Plan"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    
    # Calculate ideal weight range for height
    min_ideal_weight = 18.5 * (height_m ** 2)
    max_ideal_weight = 24.9 * (height_m ** 2)
    
    st.divider()
    st.markdown(f"<h3 style='text-align: center; color: #333;'>Your BMI: {bmi:.1f}</h3>", unsafe_allow_html=True)

    if bmi < 18.5:
        diff = min_ideal_weight - weight
        st.markdown(f"""
            <div class="card">
                <h4 style="color: #d97706; margin-top:0;">⚠️ Category: Underweight</h4>
                <p>You are approximately <b>{diff:.1f} kg</b> below the normal healthy weight range.</p>
                
                <hr style="margin: 10px 0;">
                <p><b>⏰ When to do Yoga:</b> Best time is early morning on an empty stomach, or evening (4 hours after a heavy meal).</p>
                <p><b>🌟 Recommended Yoga Asanas:</b></p>
                <ul>
                    <li><b>Bhujangasana (Cobra Pose):</b> Improves digestion and metabolism.</li>
                    <li><b>Vajrasana (Thunderbolt Pose):</b> Practice for 5-10 minutes right after meals to absorb nutrients.</li>
                </ul>
                
                <hr style="margin: 10px 0;">
                <p><b>🍽️ Daily Meal Plan (Surplus Diet):</b></p>
                <ul>
                    <li><b>Breakfast:</b> Stuffed parathas with butter/curd, a glass of full-cream milk, and a handful of dry fruits/bananas.</li>
                    <li><b>Lunch:</b> Heavy meal with multi-grain chapati, heavy dal/paneer curry, rice, and a bowl of curd.</li>
                    <li><b>Dinner:</b> Nutritious khichdi or paneer sabzi with rice/roti, followed by warm milk with ghee or turmeric.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    elif 18.5 <= bmi < 24.9:
        st.markdown(f"""
            <div class="card">
                <h4 style="color: #16a34a; margin-top:0;">✅ Category: Normal Weight</h4>
                <p>Congratulations! Your weight is completely healthy and balanced.</p>
                
                <hr style="margin: 10px 0;">
                <p><b>⏰ When to do Yoga:</b> Early morning is ideal for maintaining freshness and flexibility.</p>
                <p><b>🌟 Recommended Yoga Asanas:</b></p>
                <ul>
                    <li><b>Surya Namaskar:</b> 5-10 rounds for overall body stamina.</li>
                    <li><b>Tadasana (Mountain Pose):</b> For good posture and spinal health.</li>
                </ul>
                
                <hr style="margin: 10px 0;">
                <p><b>🍽️ Daily Meal Plan (Balanced Diet):</b></p>
                <ul>
                    <li><b>Breakfast:</b> Oats/Poha, sprouts, or eggs with fresh fruit juice.</li>
                    <li><b>Lunch:</b> Balanced portion of chapati, seasonal vegetables, dal, and a side salad.</li>
                    <li><b>Dinner:</b> Light dinner including soup, grilled vegetables, or light dal-roti (eat 2 hours before sleep).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    else:
        diff = weight - max_ideal_weight
        st.markdown(f"""
            <div class="card">
                <h4 style="color: #dc2626; margin-top:0;">ℹ️ Category: Overweight</h4>
                <p>You are approximately <b>{diff:.1f} kg</b> above the normal healthy weight range.</p>
                
                <hr style="margin: 10px 0;">
                <p><b>⏰ When to do Yoga:</b> Morning empty stomach is best for fat burning and activating metabolism.</p>
                <p><b>🌟 Recommended Yoga Asanas:</b></p>
                <ul>
                    <li><b>Kapalbhati Pranayama:</b> 10-15 minutes daily to boost metabolism and burn belly fat.</li>
                    <li><b>Dhanurasana (Bow Pose):</b> Strengthens core and stretches abdominal fat.</li>
                </ul>
                
                <hr style="margin: 10px 0;">
                <p><b>🍽️ Daily Meal Plan (Fat-Loss Diet):</b></p>
                <ul>
                    <li><b>Breakfast:</b> Warm lemon-honey water followed by green tea and sprouted moong or egg whites.</li>
                    <li><b>Lunch:</b> Large bowl of salad, 1-2 thin chapati, dal, and lots of green leafy vegetables (avoid heavy oils).</li>
                    <li><b>Dinner:</b> Light vegetable soup, boiled/roasted veggies, or light dal (finish eating before 8 PM).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

st.sidebar.markdown("### About App")
st.sidebar.info("This app provides customized wellness, meal plans, and yoga routines based on your personal body statistics.")
