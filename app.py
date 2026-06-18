import streamlit as st
import streamlit.components.v1 as components
import pickle

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="JobShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
#  AURORA BACKGROUND
# ─────────────────────────────────────────────

aurora_html = """
<style>
  .aurora-wrap {
    position: fixed;
    inset: 0;
    z-index: -1;
    overflow: hidden;
    background: #020917;
  }
  .stars {
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(1px 1px at 12% 18%, rgba(255,255,255,0.55) 0%, transparent 100%),
      radial-gradient(1px 1px at 28% 72%, rgba(255,255,255,0.45) 0%, transparent 100%),
      radial-gradient(1px 1px at 44% 35%, rgba(255,255,255,0.6)  0%, transparent 100%),
      radial-gradient(1px 1px at 61% 88%, rgba(255,255,255,0.4)  0%, transparent 100%),
      radial-gradient(1px 1px at 78% 22%, rgba(255,255,255,0.55) 0%, transparent 100%),
      radial-gradient(1px 1px at 90% 55%, rgba(255,255,255,0.5)  0%, transparent 100%),
      radial-gradient(1px 1px at  5% 90%, rgba(255,255,255,0.4)  0%, transparent 100%),
      radial-gradient(1px 1px at 35% 10%, rgba(255,255,255,0.5)  0%, transparent 100%),
      radial-gradient(1px 1px at 55% 60%, rgba(255,255,255,0.35) 0%, transparent 100%),
      radial-gradient(1px 1px at 70% 42%, rgba(255,255,255,0.45) 0%, transparent 100%),
      radial-gradient(1px 1px at 83% 78%, rgba(255,255,255,0.5)  0%, transparent 100%),
      radial-gradient(1px 1px at 18% 48%, rgba(255,255,255,0.4)  0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 50% 25%, rgba(255,255,255,0.6)  0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 22% 62%, rgba(255,255,255,0.5)  0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 76% 8%,  rgba(255,255,255,0.55) 0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 40% 80%, rgba(255,255,255,0.45) 0%, transparent 100%),
      radial-gradient(1.5px 1.5px at 95% 33%, rgba(255,255,255,0.5)  0%, transparent 100%),
      radial-gradient(1.5px 1.5px at  8% 5%,  rgba(255,255,255,0.6)  0%, transparent 100%),
      radial-gradient(2px 2px at 66% 68%, rgba(200,230,255,0.5)  0%, transparent 100%),
      radial-gradient(2px 2px at 33% 93%, rgba(200,230,255,0.4)  0%, transparent 100%),
      radial-gradient(2px 2px at 88% 14%, rgba(200,230,255,0.55) 0%, transparent 100%);
    animation: twinkle 6s ease-in-out infinite alternate;
  }
  @keyframes twinkle {
    0%   { opacity: 0.7; }
    50%  { opacity: 1;   }
    100% { opacity: 0.6; }
  }
  .orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    mix-blend-mode: screen;
  }
  .orb-1 {
    width: 65vw; height: 55vw;
    top: -20%;  left: -15%;
    background: radial-gradient(ellipse, rgba(14,80,180,0.45) 0%, transparent 70%);
    animation: drift1 20s ease-in-out infinite alternate;
  }
  .orb-2 {
    width: 55vw; height: 50vw;
    top: -10%; right: -10%;
    background: radial-gradient(ellipse, rgba(0,170,200,0.35) 0%, transparent 70%);
    animation: drift2 25s ease-in-out infinite alternate;
  }
  .orb-3 {
    width: 50vw; height: 45vw;
    bottom: -15%; left: 20%;
    background: radial-gradient(ellipse, rgba(40,0,160,0.4) 0%, transparent 70%);
    animation: drift3 22s ease-in-out infinite alternate;
  }
  .orb-4 {
    width: 40vw; height: 40vw;
    top: 30%;  right: 5%;
    background: radial-gradient(ellipse, rgba(0,200,160,0.2) 0%, transparent 70%);
    animation: drift4 18s ease-in-out infinite alternate;
  }
  .orb-5 {
    width: 35vw; height: 35vw;
    top: 50%;  left: 35%;
    background: radial-gradient(ellipse, rgba(80,20,200,0.25) 0%, transparent 70%);
    animation: drift5 28s ease-in-out infinite alternate;
  }
  .aurora-band {
    position: absolute;
    left: -10%;
    width: 120%;
    height: 180px;
    top: 15%;
    background: linear-gradient(180deg,
      transparent 0%,
      rgba(0,160,220,0.07) 30%,
      rgba(20,80,200,0.1) 50%,
      rgba(0,200,180,0.07) 70%,
      transparent 100%
    );
    filter: blur(20px);
    animation: bandMove 16s ease-in-out infinite alternate;
  }
  @keyframes bandMove {
    0%   { top: 10%; opacity: 0.5; transform: skewY(-1deg);   }
    50%  { top: 20%; opacity: 1;   transform: skewY(1deg);    }
    100% { top: 12%; opacity: 0.6; transform: skewY(-0.5deg); }
  }
  .grid-overlay {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(56,189,248,0.025) 1px, transparent 1px),
      linear-gradient(90deg, rgba(56,189,248,0.025) 1px, transparent 1px);
    background-size: 60px 60px;
  }
  @keyframes drift1 {
    0%   { transform: translate(0,  0)   scale(1);    }
    100% { transform: translate(6%, 8%)  scale(1.08); }
  }
  @keyframes drift2 {
    0%   { transform: translate(0,   0)   scale(1);   }
    100% { transform: translate(-8%, 5%)  scale(1.1); }
  }
  @keyframes drift3 {
    0%   { transform: translate(0,   0)   scale(1);    }
    100% { transform: translate(5%, -6%)  scale(1.06); }
  }
  @keyframes drift4 {
    0%   { transform: translate(0,   0)   scale(1);    }
    100% { transform: translate(-5%, 8%)  scale(1.12); }
  }
  @keyframes drift5 {
    0%   { transform: translate(0,   0)   scale(1);    }
    100% { transform: translate(4%, -4%)  scale(0.92); }
  }
</style>
<div class="aurora-wrap">
  <div class="stars"></div>
  <div class="aurora-band"></div>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
  <div class="orb orb-4"></div>
  <div class="orb orb-5"></div>
  <div class="grid-overlay"></div>
</div>
"""
components.html(aurora_html, height=0)

# ─────────────────────────────────────────────
#  LOAD MODEL
# ─────────────────────────────────────────────

@st.cache_resource(show_spinner="Loading AI model...")
def load_model():
    from pathlib import Path
    base_dir = Path(__file__).parent

    model_path = base_dir / "model.pkl"
    vectorizer_path = base_dir / "vectorizer.pkl"

    if not model_path.exists():
        st.error("model.pkl is missing. Please upload model.pkl to your GitHub repository/project folder.")
        st.stop()

    if not vectorizer_path.exists():
        st.error("vectorizer.pkl is missing. Please upload vectorizer.pkl to your GitHub repository/project folder.")
        st.stop()

    try:
        with open(model_path, "rb") as f:
            model = pickle.load(f)

        with open(vectorizer_path, "rb") as f:
            vectorizer = pickle.load(f)

        return model, vectorizer

    except Exception as e:
        st.error(f"Model loading error: {e}")
        st.stop()

model, vectorizer = load_model()
model_loaded = model is not None and vectorizer is not None

# ─────────────────────────────────────────────
#  BETTER FAKE DETECTION HELPERS
# ─────────────────────────────────────────────

def calculate_rule_risk(text):
    text = text.lower()

    high_risk_keywords = [
        "registration fee", "security deposit", "processing fee", "verification fee",
        "pay", "upi", "telegram", "whatsapp", "no interview", "guaranteed income",
        "instant joining", "limited seats", "bank details", "aadhaar", "investment",
        "refundable deposit", "no experience required", "earn daily", "earn weekly"
    ]

    score = 0
    matched = []

    for word in high_risk_keywords:
        if word in text:
            score += 1
            matched.append(word)

    return score, matched


# ─────────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>

/* ── APP BACKGROUND — transparent so aurora shows ── */
.stApp {
    background: transparent !important;
    color: white;
}

.stApp > div {
    background: transparent !important;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem !important; }

/* ── TYPOGRAPHY ── */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');

/* Main title — elegant serif with light gradient */
.main-title {
    font-family: 'Outfit', sans-serif;
    font-size: clamp(30px, 5vw, 54px);
    font-weight: 800;
    font-style: normal;
    letter-spacing: -1.5px;
    line-height: 1.05;
    margin-bottom: 4px;
    background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 40%, #7dd3fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* Subtitle — airy, spaced uppercase */
.subtitle {
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    font-weight: 400;
    color: #64748b;
    margin-top: 8px;
    letter-spacing: 0.2px;
    line-height: 1.5;
}

/* ── GLASS CARD ── */
.glass-card {
    background: rgba(14, 26, 50, 0.6);
    border: 1px solid rgba(56, 189, 248, 0.12);
    border-radius: 24px;
    padding: 32px;
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    box-shadow: 0 0 0 1px rgba(56,189,248,0.05), inset 0 1px 0 rgba(255,255,255,0.04);
    margin-bottom: 20px;
}

/* ── SECTION HEADER ── */
.section-header {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    color: #38bdf8;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    opacity: 0.8;
}

.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(126,184,212,0.25), transparent);
}

/* ── TEXTAREA ── */
.stTextArea textarea {
    background: rgba(2, 8, 20, 0.85) !important;
    color: #e2e8f0 !important;
    border: 1.5px solid rgba(56,189,248,0.2) !important;
    border-radius: 16px !important;
    padding: 18px !important;
    font-size: 15px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 300 !important;
    min-height: 220px !important;
    transition: border-color 0.3s !important;
    resize: vertical !important;
}

.stTextArea textarea:focus {
    border-color: rgba(56,189,248,0.6) !important;
    box-shadow: 0 0 0 3px rgba(56,189,248,0.08) !important;
}

/* ── ANALYZE BUTTON ── */
.stButton > button {
    width: 100% !important;
    height: 56px !important;
    border-radius: 12px !important;
    background: linear-gradient(90deg, #0369a1, #0891b2) !important;
    color: #f0f9ff !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border: 1px solid rgba(56,189,248,0.2) !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 2px 16px rgba(8,145,178,0.2) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(8,145,178,0.5) !important;
    background: linear-gradient(90deg, #0284c7, #06b6d4) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── FEATURE CARDS ── */
.feature-card {
    background: rgba(14, 26, 50, 0.5);
    border: 1px solid rgba(56,189,248,0.1);
    border-radius: 20px;
    padding: 28px 18px;
    text-align: center;
    font-family: 'Inter', sans-serif;
    transition: all 0.3s ease;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #38bdf8, #22d3ee, transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.feature-card:hover {
    transform: translateY(-6px);
    border-color: rgba(56,189,248,0.3);
    box-shadow: 0 12px 40px rgba(0,0,0,0.3), 0 0 0 1px rgba(56,189,248,0.1);
}

.feature-card:hover::before { opacity: 1; }

.feature-icon { font-size: 38px; margin-bottom: 14px; }

.feature-card h3 {
    font-family: 'Outfit', sans-serif;
    font-size: 13px;
    font-weight: 700;
    color: #e2e8f0;
    letter-spacing: 0.2px;
    margin-bottom: 10px;
}

.feature-card p {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 300;
    color: #4e6e84;
    line-height: 1.7;
    margin: 0;
}

/* ── RESULT CARD ── */
.result-fake {
    padding: 20px 28px;
    border-radius: 14px;
    text-align: center;
    margin-top: 24px;
    font-family: 'Outfit', sans-serif;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.3px;
    background: rgba(239, 68, 68, 0.08);
    border: 1px solid rgba(239,68,68,0.3);
    color: #fca5a5;
    box-shadow: 0 0 24px rgba(239,68,68,0.1);
    animation: resultPop 0.4s cubic-bezier(0.16,1,0.3,1);
}

.result-real {
    padding: 20px 28px;
    border-radius: 14px;
    text-align: center;
    margin-top: 24px;
    font-family: 'Outfit', sans-serif;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.3px;
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16,185,129,0.3);
    color: #6ee7b7;
    box-shadow: 0 0 24px rgba(16,185,129,0.1);
    animation: resultPop 0.4s cubic-bezier(0.16,1,0.3,1);
}

@keyframes resultPop {
    from { opacity: 0; transform: scale(0.96) translateY(8px); }
    to   { opacity: 1; transform: scale(1) translateY(0); }
}

/* ── CONFIDENCE BAR ── */
.conf-bar-wrap {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    overflow: hidden;
    height: 8px;
    margin-top: 8px;
}

.conf-bar-fill-fake {
    height: 100%;
    border-radius: 8px;
    background: linear-gradient(90deg, #ef4444, #f87171);
    transition: width 1s cubic-bezier(0.16,1,0.3,1);
}

.conf-bar-fill-real {
    height: 100%;
    border-radius: 8px;
    background: linear-gradient(90deg, #10b981, #34d399);
    transition: width 1s cubic-bezier(0.16,1,0.3,1);
}

/* ── METRIC CARD ── */
.metric-card {
    background: rgba(14, 26, 50, 0.6);
    border: 1px solid rgba(56,189,248,0.1);
    border-radius: 16px;
    padding: 22px 20px;
    text-align: center;
    font-family: 'Inter', sans-serif;
}

.metric-label {
    font-family: 'Inter', sans-serif;
    font-size: 10px;
    font-weight: 400;
    letter-spacing: 3.5px;
    text-transform: uppercase;
    color: #4a6a82;
    margin-bottom: 10px;
}

.metric-value {
    font-family: 'Outfit', sans-serif;
    font-size: 36px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1;
}

.metric-value-fake { color: #f87171; }
.metric-value-real { color: #34d399; }

/* ── WARNING BANNER ── */
.warn-banner {
    background: rgba(245,158,11,0.08);
    border: 1px solid rgba(245,158,11,0.25);
    border-radius: 12px;
    padding: 14px 18px;
    font-size: 13px;
    color: #fbbf24;
    font-family: 'Inter', sans-serif;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* ── TIPS LIST ── */
.tip-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    color: #8aa4be;
    line-height: 1.7;
    font-weight: 300;
}

.tip-item:last-child { border-bottom: none; }

.tip-icon {
    font-size: 18px;
    flex-shrink: 0;
    margin-top: 1px;
}

/* ── SETTINGS ── */
.settings-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-family: 'Inter', sans-serif;
}

.settings-label {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    color: #c8daea;
    font-weight: 500;
    letter-spacing: 0.2px;
}

.settings-sub {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 300;
    color: #3d5a6e;
    margin-top: 3px;
    letter-spacing: 0.5px;
}

.badge-on {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    color: #34d399;
    padding: 4px 12px;
    border-radius: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 1px;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    color: #1e3a4a;
    font-size: 11px;
    margin-top: 60px;
    padding-bottom: 40px;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px !important;
    background: rgba(14,26,50,0.6) !important;
    padding: 5px !important;
    border-radius: 14px !important;
    border: 1px solid rgba(56,189,248,0.12) !important;
    flex-wrap: wrap !important;
    overflow-x: auto !important;
    scrollbar-width: none !important;
}

.stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
    display: none !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 10px !important;
    padding: 8px 14px !important;
    color: #475569 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.2s !important;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
    min-width: 0 !important;
}

.stTabs [aria-selected="true"] {
    background: rgba(56,189,248,0.12) !important;
    color: #38bdf8 !important;
    border: 1px solid rgba(56,189,248,0.25) !important;
}

/* Mobile tabs */
@media (max-width: 480px) {
    .stTabs [data-baseweb="tab-list"] {
        gap: 3px !important;
        padding: 4px !important;
        border-radius: 12px !important;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 7px 10px !important;
        font-size: 11px !important;
        letter-spacing: 0 !important;
    }
}

/* ── PROGRESS BAR ── */
.stProgress > div > div > div {
    background: linear-gradient(90deg, #0369a1, #22d3ee) !important;
    border-radius: 4px !important;
}

.stProgress > div > div {
    background: rgba(255,255,255,0.05) !important;
    border-radius: 4px !important;
}

/* ── MOBILE ── */
@media (max-width: 768px) {
    .main-title { font-size: 32px; letter-spacing: -0.5px; }
    .subtitle { font-size: 14px; }
    .glass-card { padding: 16px 14px; border-radius: 16px; }
    .section-header { font-size: 12px; }
    .feature-card { padding: 18px 14px; min-height: 160px; }
    .feature-icon { font-size: 28px; margin-bottom: 8px; }
    .feature-card h3 { font-size: 11px; }
    .feature-card p { font-size: 12px; }
    .metric-value { font-size: 26px; }
    .result-fake, .result-real { font-size: 15px; padding: 16px 14px; letter-spacing: 0.5px; }
    .block-container { padding-left: 0.5rem !important; padding-right: 0.5rem !important; padding-top: 1rem !important; }
    .tip-item { font-size: 13px; }
}

@media (max-width: 400px) {
    .main-title { font-size: 26px; }
    .result-fake, .result-real { font-size: 13px; }
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────

col_logo, col_title = st.columns([1, 6])

with col_logo:
    try:
        st.image("logo.png", width=120)
    except Exception:
        st.markdown("<div style='font-size:64px;text-align:center;padding-top:4px;'>🛡️</div>", unsafe_allow_html=True)

with col_title:
    st.markdown('<div class="main-title">JobShield AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-powered Fake Job Posting Detection System</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────

tab_home, tab_analyze, tab_tips, tab_settings = st.tabs([
    "🏠 Home",
    "🔍 Analyze",
    "💡 Tips",
    "⚙️ Settings"
])

# ═══════════════════════════════════════════════
#  HOME TAB
# ═══════════════════════════════════════════════

with tab_home:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Platform Features</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    features = [
        ("🛡️", "Smart Detection",   "Advanced ML model detects fake job postings with high precision using NLP."),
        ("⚡", "Instant Results",   "Analyze any job description and get a confidence score in under a second."),
        ("🎯", "High Accuracy",     "Trained on thousands of verified real & fraudulent job listings."),
        ("🧠", "NLP Engine",        "Natural Language Processing understands intent, tone, and red-flag phrases."),
    ]

    for col, (icon, title, desc) in zip([c1, c2, c3, c4], features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── How it works ──
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">How It Works</div>', unsafe_allow_html=True)

    s1, s2, s3 = st.columns(3)

    steps = [
        ("01", "#38bdf8", "Paste Job Description", "Copy any job posting — title, description, requirements, salary, contact details."),
        ("02", "#22d3ee", "AI Analyzes Text",       "Our NLP model scans for 50+ fraud signals including fee requests, vague roles, and suspicious promises."),
        ("03", "#10b981", "Get Verdict",            "See Fake / Real score instantly with confidence percentages to make an informed decision."),
    ]

    for col, (num, color, title, desc) in zip([s1, s2, s3], steps):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div style="font-family:'Plus Jakarta Sans',sans-serif;font-size:38px;font-weight:800;color:{color};margin-bottom:10px;">{num}</div>
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
#  ANALYZE TAB
# ═══════════════════════════════════════════════

with tab_analyze:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">📄 Enter Job Description</div>', unsafe_allow_html=True)

    job_text = st.text_area(
        label="",
        placeholder="Paste the complete job posting here...\n\nInclude: job title, responsibilities, salary, requirements, contact details — everything you see in the posting.",
        height=220,
        key="job_input"
    )

    char_count = len(job_text.strip())
    if char_count > 0:
        st.caption(f"📝 {char_count} characters · {len(job_text.split())} words")

    btn_col, _ = st.columns([2, 1])
    with btn_col:
        analyze_clicked = st.button("🔍  ANALYZE JOB POSTING", key="analyze_btn")

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Results ──
    if analyze_clicked:

        if job_text.strip() == "":
            st.markdown("""
            <div class="warn-banner">
                ⚠️ &nbsp; Please enter a job description before analyzing.
            </div>
            """, unsafe_allow_html=True)

        else:
            with st.spinner("Scanning for fraud signals..."):
                data = vectorizer.transform([job_text])
                raw_prediction = model.predict(data)[0]
                proba = model.predict_proba(data)[0]

                # Raw model scores
                raw_fake_pct = proba[1] * 100
                raw_real_pct = proba[0] * 100

                rule_score, matched_keywords = calculate_rule_risk(job_text)

                # Adjusted hybrid score: model probability + rule-based risk signals.
                # IMPORTANT: final prediction is based on the adjusted score,
                # so Fake/Real result and displayed scores stay consistent.
                fake_pct = raw_fake_pct + (rule_score * 18)

                # Strong suspicious signals should clearly push the score into fake range.
                if rule_score >= 2:
                    fake_pct = max(fake_pct, 65)
                elif rule_score == 1:
                    fake_pct = max(fake_pct, 52)

                # If the trained model itself predicts fake, keep fake confidence above 50.
                if int(raw_prediction) == 1:
                    fake_pct = max(fake_pct, 58)

                fake_pct = min(100, max(0, fake_pct))
                real_pct = 100 - fake_pct

                # Final decision: Fake only when fake score is higher than real score.
                prediction = 1 if fake_pct >= 50 else 0

            # Scores
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-header">📊 AI Confidence Scores</div>', unsafe_allow_html=True)

            m1, m2 = st.columns(2)

            with m1:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">🚨 Fake Score</div>
                    <div class="metric-value metric-value-fake">{fake_pct:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(int(fake_pct))

            with m2:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-label">✅ Real Score</div>
                    <div class="metric-value metric-value-real">{real_pct:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
                st.progress(int(real_pct))

            # Verdict
            if int(prediction) == 1:
                st.markdown("""
                <div class="result-fake">
                    🚨 &nbsp; FAKE JOB POSTING DETECTED
                </div>
                """, unsafe_allow_html=True)
                st.warning("⚠️ Do NOT apply or share any personal/banking information. Report this posting to the platform.")
            else:
                st.markdown("""
                <div class="result-real">
                    ✅ &nbsp; REAL JOB POSTING
                </div>
                """, unsafe_allow_html=True)
                st.success("✅ This posting appears legitimate. Still verify the company independently before applying.")

            st.markdown('</div>', unsafe_allow_html=True)

            # Risk breakdown
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-header">📈 Risk Breakdown</div>', unsafe_allow_html=True)

            risk_level = "HIGH RISK" if fake_pct >= 70 else "MEDIUM RISK" if fake_pct >= 50 else "LOW RISK"
            risk_color = "#ef4444" if fake_pct >= 70 else "#f59e0b" if fake_pct >= 50 else "#10b981"

            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span style="font-size:13px;color:#475569;font-family:'Inter', sans-serif;font-weight:300;">Overall Fraud Risk</span>
                <span style="font-family:'Inter', sans-serif;font-size:13px;font-weight:600;letter-spacing:1px;color:{risk_color};">{risk_level}</span>
            </div>
            """, unsafe_allow_html=True)
            st.progress(int(fake_pct))

            st.markdown(f"""
            <div style="margin-top:16px;font-family:'Inter', sans-serif;font-size:13px;color:#52728a;line-height:1.7;font-weight:300;">
                Final confidence: <span style="color:#e2e8f0;font-weight:600;">{max(fake_pct, real_pct):.1f}%</span> &nbsp;·&nbsp;
                Raw model fake score: <span style="color:#e2e8f0;font-weight:600;">{raw_fake_pct:.1f}%</span> &nbsp;·&nbsp;
                Prediction: <span style="color:{risk_color};font-weight:600;">{'Fraudulent' if prediction == 1 else 'Legitimate'}</span>
            </div>
            """, unsafe_allow_html=True)

            if matched_keywords:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<div class='section-header'>⚠️ Suspicious Signals Found</div>", unsafe_allow_html=True)
                clean_words = ", ".join(sorted(set(matched_keywords))[:8])
                st.markdown(f"""
                <div class="warn-banner">
                    Detected risky terms: <b>{clean_words}</b>
                </div>
                """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
#  TIPS TAB
# ═══════════════════════════════════════════════

with tab_tips:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🚨 Red Flags to Watch</div>', unsafe_allow_html=True)

    red_flags = [
        ("💸", "<b>Upfront payment required</b> — Registration fee, training fee, or equipment deposit. Legitimate employers never charge candidates."),
        ("📧", "<b>Personal email domains</b> — Gmail/Yahoo addresses for corporate job offers. Real companies use official domains."),
        ("⚡", "<b>Urgency tactics</b> — 'Apply within 24 hours', 'Only 3 seats left'. Designed to stop you from thinking critically."),
        ("💰", "<b>Unrealistic salary</b> — ₹50,000/week with no experience? High pay for low-skill tasks is a classic fraud hook."),
        ("🔒", "<b>Personal info upfront</b> — Asking for Aadhaar, bank account, or passport before any interview."),
        ("📞", "<b>Only WhatsApp contact</b> — No official office address, no company website, no landline."),
        ("✍️",  "<b>Vague job description</b> — No clear responsibilities, generic 'earn from home' type postings."),
        ("📸", "<b>Unrelated photo requests</b> — Asking for personal photos unrelated to the role is a grooming tactic."),
    ]

    for icon, text in red_flags:
        st.markdown(f'<div class="tip-item"><span class="tip-icon">{icon}</span><span>{text}</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">✅ How to Stay Safe</div>', unsafe_allow_html=True)

    safe_tips = [
        ("🔍", "Verify the company on <b>MCA India portal</b> (mca.gov.in) or LinkedIn before applying."),
        ("🌐", "Check if the company website is real and professional — fake sites often have poor design or no content."),
        ("📋", "Legitimate hiring always has a proper interview process. Instant 'selected!' messages are a red flag."),
        ("🤝", "Never pay money to get a job — this is illegal under many labour laws."),
        ("📱", "Search the job posting text in Google — scammers often reuse the same text across many platforms."),
        ("👥", "Talk to someone you trust before accepting offers that seem too good to be true."),
    ]

    for icon, text in safe_tips:
        st.markdown(f'<div class="tip-item"><span class="tip-icon">{icon}</span><span>{text}</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════
#  SETTINGS TAB
# ═══════════════════════════════════════════════

with tab_settings:

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⚙️ System Status</div>', unsafe_allow_html=True)

    status_rows = [
        ("System Online",        "All services running normally",   "ON"),
        ("AI Detection Engine",  "Model loaded and ready",          "ON"),
        ("NLP Vectorizer",       "Text processing active",          "ON"),
        ("Real-time Analysis",   "Sub-second inference enabled",    "ON"),
    ]

    for label, sub, badge in status_rows:
        st.markdown(f"""
        <div class="settings-row">
            <div>
                <div class="settings-label">{label}</div>
                <div class="settings-sub">{sub}</div>
            </div>
            <span class="badge-on">{badge}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">ℹ️ About</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Inter', sans-serif;font-size:14px;color:#52728a;font-weight:300;line-height:1.8;">
        <b style="color:#e2e8f0;">JobShield AI</b> is a machine learning-powered fake job detection system 
        trained on thousands of real and fraudulent job postings using TF-IDF vectorization 
        and a classification model.<br><br>
        Built to protect job seekers from online fraud, phishing, and financial scams 
        disguised as employment opportunities.<br><br>
        <span style="color:#38bdf8;font-family:'JetBrains Mono', monospace;font-size:12px;letter-spacing:1px;">
        </span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)




# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────

st.markdown("""
<div class="footer">
    JobShield AI &nbsp;·&nbsp; Made by Chandan &nbsp;·&nbsp; Protecting Job Seekers
</div>
""", unsafe_allow_html=True)