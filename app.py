import streamlit as st
import pickle

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD MODEL ----------------

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Main Background */

.stApp {
    background: linear-gradient(135deg, #020617, #071226, #0f172a);
    color: white;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: rgba(5, 10, 25, 0.95);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar Text */

section[data-testid="stSidebar"] * {
    color: white;
}

/* Hide Streamlit Branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Title */

.main-title {
    font-size: 65px;
    font-weight: 900;
    background: linear-gradient(to right, #38bdf8, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0px;
}

/* Subtitle */

.subtitle {
    color: #94a3b8;
    font-size: 22px;
    margin-top: -10px;
}

/* Glass Card */

.glass-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 30px;
    padding: 30px;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 40px rgba(0,0,0,0.4);
}

/* Text Area */

.stTextArea textarea {
    background: rgba(2,6,23,0.9);
    color: white;
    border: 2px solid #0ea5e9;
    border-radius: 20px;
    padding: 20px;
    font-size: 18px;
    min-height: 250px;
}

/* Button */

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

/* Result Card */

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

    animation: popup 0.4s ease;
}

/* Fake */

.fake {
    background: rgba(255,0,0,0.1);
    border: 2px solid rgba(255,0,0,0.5);
    color: #ff4d4d;
    box-shadow: 0 0 20px rgba(255,0,0,0.3);
}

/* Real */

.real {
    background: rgba(0,255,127,0.1);
    border: 2px solid rgba(0,255,127,0.5);
    color: #22c55e;
    box-shadow: 0 0 20px rgba(34,197,94,0.3);
}

/* Feature Cards */

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

    overflow: hidden;
}

.feature-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 0 30px rgba(56,189,248,0.3);
}

/* Feature Card Heading */

.feature-card h2 {
    font-size: 22px;
    margin-top: 15px;
    margin-bottom: 15px;
    line-height: 1.3;
}

/* Feature Card Paragraph */

.feature-card p {
    font-size: 16px;
    color: #cbd5e1;
    line-height: 1.6;
}

/* Metrics */

.metric-card {
    background: rgba(255,255,255,0.04);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    margin-top: 10px;
}

/* Footer */

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

/* Animation */

@keyframes popup {

    0% {
        transform: scale(0.8);
        opacity: 0;
    }

    100% {
        transform: scale(1);
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.image("logo.png", width=220)

st.sidebar.markdown("# 🛡️ JobShield AI")

st.sidebar.markdown("""
### Navigation

- 🏠 Home
- 📊 Analyze Job
- 📁 Saved Results
- ⚙️ Settings

---

### Features

✅ AI Detection  
✅ Real-time Analysis  
✅ High Accuracy  
✅ NLP Technology  

---

### Tech Stack

- Python
- Streamlit
- Machine Learning
- NLP
- Scikit-learn
""")

st.sidebar.success("🟢 System Online")

# ---------------- MADE BY ----------------

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <div style="
        text-align:center;
        padding:12px;
        border-radius:15px;
        background:rgba(255,255,255,0.05);
        color:white;
        font-size:18px;
        font-weight:bold;
    ">
        Made by Chandan 🚀
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ----------------

col1, col2 = st.columns([1,5])

with col1:
    st.image("logo.png", width=180)

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

# ---------------- MAIN CARD ----------------

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown("## 📄 Enter Job Description")

job_text = st.text_area(
    "",
    placeholder="Paste complete job description here..."
)

# ---------------- BUTTON ----------------

if st.button("🔍 Analyze Job Posting"):

    if job_text.strip() == "":

        st.warning("Please enter job description")

    else:

        # Transform
        data = vectorizer.transform([job_text])

        # Prediction
        prediction = model.predict(data)

        # Probability
        probability = model.predict_proba(data)

        fake_score = probability[0][1] * 100
        real_score = probability[0][0] * 100

        # ---------------- SCORES ----------------

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

        # ---------------- RESULT ----------------

        if int(prediction[0]) == 1:

            st.markdown(f"""
            <div class="result-card fake">
            🚨 Fake Job Posting Detected
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown(f"""
            <div class="result-card real">
            ✅ Real Job Posting
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FEATURE SECTION ----------------

st.write("")
st.write("")

st.markdown("## 🚀 Platform Features")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h1>🛡️</h1>
    <h2>Smart Detection</h2>
    <p>
    Advanced AI model detects fake job postings
    with high accuracy.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h1>⚡</h1>
    <h2>Instant Results</h2>
    <p>
    Get prediction and confidence scores
    instantly.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h1>🎯</h1>
    <h2>High Accuracy</h2>
    <p>
    Trained on thousands of real & fake
    job postings.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
    <h1>🧠</h1>
    <h2>NLP Technology</h2>
    <p>
    Uses Natural Language Processing
    for analysis.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------

st.markdown("""
<div class="footer">
Made by Chandan
</div>
""", unsafe_allow_html=True)