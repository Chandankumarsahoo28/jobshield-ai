import streamlit as st
import streamlit.components.v1 as components
import pickle

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- PARTICLES BACKGROUND ---------------- #

particles_html = """
<div id="particles-js"></div>

<style>

#particles-js {
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
    top: 0;
    left: 0;
}

</style>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>

<script>
particlesJS("particles-js", {

  "particles": {

    "number": {
      "value": 70
    },

    "color": {
      "value": "#38bdf8"
    },

    "shape": {
      "type": "circle"
    },

    "opacity": {
      "value": 0.5
    },

    "size": {
      "value": 3
    },

    "line_linked": {
      "enable": true,
      "distance": 150,
      "color": "#38bdf8",
      "opacity": 0.4,
      "width": 1
    },

    "move": {
      "enable": true,
      "speed": 2
    }
  }

});
</script>
"""

components.html(particles_html, height=0)

# ---------------- LOAD MODEL ---------------- #

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* ---------------- APP BACKGROUND ---------------- */

.stApp {

    background: linear-gradient(
    -45deg,
    #020617,
    #071226,
    #0f172a,
    #1e3a8a
    );

    background-size: 400% 400%;

    animation: gradient 15s ease infinite;

    color: white;
}

/* ---------------- ANIMATION ---------------- */

@keyframes gradient {

0% {
background-position: 0% 50%;
}

50% {
background-position: 100% 50%;
}

100% {
background-position: 0% 50%;
}

}

/* ---------------- HIDE STREAMLIT ---------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ---------------- TITLE ---------------- */

.main-title {

    font-size: 65px;

    font-weight: 900;

    background: linear-gradient(to right, #38bdf8, #22d3ee);

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 0px;
}

/* ---------------- SUBTITLE ---------------- */

.subtitle {

    color: #94a3b8;

    font-size: 22px;

    margin-top: -10px;
}

/* ---------------- GLASS CARD ---------------- */

.glass-card {

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 30px;

    padding: 30px;

    backdrop-filter: blur(20px);

    box-shadow: 0 0 40px rgba(0,0,0,0.4);
}

/* ---------------- TEXT AREA ---------------- */

.stTextArea textarea {

    background: rgba(2,6,23,0.9);

    color: white;

    border: 2px solid #0ea5e9;

    border-radius: 20px;

    padding: 20px;

    font-size: 18px;

    min-height: 250px;
}

/* ---------------- BUTTON ---------------- */

.stButton button {

    width: 100%;

    height: 65px;

    border: none;

    border-radius: 18px;

    background: linear-gradient(to right, #2563eb, #06b6d4);

    color: white;

    font-size: 24px;

    font-weight: bold;

    transition: 0.4s;

    box-shadow: 0 0 25px rgba(37,99,235,0.5);
}

.stButton button:hover {

    transform: scale(1.02);

    box-shadow: 0 0 35px rgba(6,182,212,0.8);
}

/* ---------------- RESULT CARD ---------------- */

.result-card {

    padding: 18px;

    border-radius: 18px;

    text-align: center;

    margin-top: 20px;

    font-size: 22px;

    font-weight: bold;

    width: 75%;

    margin-left: auto;

    margin-right: auto;
}

/* ---------------- FAKE ---------------- */

.fake {

    background: rgba(255,0,0,0.1);

    border: 2px solid rgba(255,0,0,0.5);

    color: #ff4d4d;

    box-shadow: 0 0 20px rgba(255,0,0,0.3);
}

/* ---------------- REAL ---------------- */

.real {

    background: rgba(0,255,127,0.1);

    border: 2px solid rgba(0,255,127,0.5);

    color: #22c55e;

    box-shadow: 0 0 20px rgba(34,197,94,0.3);
}

/* ---------------- FEATURE CARD ---------------- */

.feature-card {

    background: rgba(255,255,255,0.04);

    border-radius: 20px;

    padding: 25px;

    text-align: center;

    border: 1px solid rgba(255,255,255,0.08);

    transition: 0.3s;

    min-height: 320px;

    display: flex;

    flex-direction: column;

    justify-content: flex-start;

    align-items: center;
}

.feature-card:hover {

    transform: translateY(-8px);

    box-shadow: 0 0 30px rgba(56,189,248,0.3);
}

/* ---------------- FEATURE TEXT ---------------- */

.feature-card h2 {

    font-size: 22px;

    margin-top: 15px;

    margin-bottom: 15px;

    line-height: 1.3;
}

.feature-card p {

    font-size: 16px;

    color: #cbd5e1;

    line-height: 1.6;
}

/* ---------------- METRIC CARD ---------------- */

.metric-card {

    background: rgba(255,255,255,0.04);

    border-radius: 20px;

    padding: 20px;

    text-align: center;

    margin-top: 10px;
}

/* ---------------- TABS ---------------- */

.stTabs [data-baseweb="tab-list"] {

    gap: 15px;

    justify-content: center;
}

.stTabs [data-baseweb="tab"] {

    background: rgba(255,255,255,0.05);

    border-radius: 12px;

    padding: 12px 22px;

    color: white;

    font-size: 16px;

    font-weight: 600;
}

/* ---------------- FOOTER ---------------- */

.footer {

    text-align: center;

    color: gray;

    margin-top: 50px;
}

/* ---------------- MOBILE ---------------- */

@media screen and (max-width: 768px) {

    .main-title {
        font-size: 42px;
    }

    .subtitle {
        font-size: 17px;
    }

    .glass-card {
        padding: 20px;
    }

    .feature-card {
        min-height: auto;
    }

    .result-card {
        width: 100%;
        font-size: 18px;
    }

    .stButton button {
        height: 55px;
        font-size: 18px;
    }

    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

col1, col2 = st.columns([1,5])

with col1:
    st.image("logo.png", width=140)

with col2:

    st.markdown(
        '<div class="main-title">JobShield AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">AI-powered Fake Job Posting Detection System</div>',
        unsafe_allow_html=True
    )

st.write("")

# ---------------- TOP TABS ---------------- #

tab1, tab2, tab3 = st.tabs([
    "🏠 Home",
    "📊 Analyze",
    "⚙️ Settings"
])

# ================= HOME TAB ================= #

with tab1:

    st.markdown("## 🚀 Platform Features")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h1>🛡️</h1>
        <h2>Smart Detection</h2>
        <p>
        Advanced AI model detects fake job postings with high accuracy.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h1>⚡</h1>
        <h2>Instant Results</h2>
        <p>
        Get prediction and confidence scores instantly.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <h1>🎯</h1>
        <h2>High Accuracy</h2>
        <p>
        Trained on thousands of real & fake job postings.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card">
        <h1>🧠</h1>
        <h2>NLP Technology</h2>
        <p>
        Uses Natural Language Processing for analysis.
        </p>
        </div>
        """, unsafe_allow_html=True)

# ================= ANALYZE TAB ================= #

with tab2:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown("## 📄 Enter Job Description")

    job_text = st.text_area(
        "",
        placeholder="Paste complete job description here..."
    )

    if st.button("🔍 Analyze Job Posting"):

        if job_text.strip() == "":

            st.warning("Please enter job description")

        else:

            data = vectorizer.transform([job_text])

            prediction = model.predict(data)

            probability = model.predict_proba(data)

            fake_score = probability[0][1] * 100
            real_score = probability[0][0] * 100

            st.markdown("## 📊 AI Confidence Scores")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(f"""
                <div class="metric-card">
                    <h2>🚨 Fake Score</h2>
                    <h1>{fake_score:.2f}%</h1>
                </div>
                """, unsafe_allow_html=True)

                st.progress(int(fake_score))

            with col2:

                st.markdown(f"""
                <div class="metric-card">
                    <h2>✅ Real Score</h2>
                    <h1>{real_score:.2f}%</h1>
                </div>
                """, unsafe_allow_html=True)

                st.progress(int(real_score))

            if int(prediction[0]) == 1:

                st.markdown("""
                <div class="result-card fake">
                🚨 Fake Job Posting Detected
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown("""
                <div class="result-card real">
                ✅ Real Job Posting
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ================= SETTINGS TAB ================= #

with tab3:

    st.markdown("""
    <div class="glass-card">

    <h2>⚙️ Settings</h2>

    <p style="color:#cbd5e1;font-size:18px;">

    ✅ System Online  
    <br><br>

    ✅ AI Detection Enabled  
    <br><br>

    ✅ NLP Engine Active

    <br><br><br>

    Made by Chandan 🚀

    </p>

    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class="footer">

MADE BY CHANDAN

</div>
""", unsafe_allow_html=True)