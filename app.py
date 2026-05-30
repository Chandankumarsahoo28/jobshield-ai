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
#  PARTICLES BACKGROUND
# ─────────────────────────────────────────────

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
    "number": { "value": 55 },
    "color": { "value": "#38bdf8" },
    "shape": { "type": "circle" },
    "opacity": { "value": 0.35 },
    "size": { "value": 2.5 },
    "line_linked": {
      "enable": true,
      "distance": 140,
      "color": "#38bdf8",
      "opacity": 0.25,
      "width": 1
    },
    "move": { "enable": true, "speed": 1.5 }
  }
});
</script>
"""
components.html(particles_html, height=0)

# ─────────────────────────────────────────────
#  LOAD MODEL
# ─────────────────────────────────────────────

@st.cache_resource
def load_model():
    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

# ─────────────────────────────────────────────
#  CUSTOM CSS
# ─────────────────────────────────────────────

st.markdown("""
<style>

/* ── APP BACKGROUND ── */
.stApp {
    background: linear-gradient(-45deg, #020617, #060f22, #0c1a3a, #071828);
    background-size: 400% 400%;
    animation: gradient 18s ease infinite;
    color: white;
}

@keyframes gradient {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ── HIDE STREAMLIT CHROME ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem !important; }

/* ── TYPOGRAPHY ── */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Inter:wght@400;500;600&display=swap');

.main-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(38px, 6vw, 68px);
    font-weight: 900;
    background: linear-gradient(90deg, #38bdf8, #22d3ee, #67e8f9);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
    line-height: 1.1;
    margin-bottom: 4px;
}

.subtitle {
    color: #64748b;
    font-size: 18px;
    margin-top: 6px;
    font-family: 'Inter', sans-serif;
    font-weight: 400;
    letter-spacing: 0.2px;
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
    font-family: 'Orbitron', monospace;
    font-size: 15px;
    font-weight: 700;
    color: #38bdf8;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(56,189,248,0.3), transparent);
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
    height: 60px !important;
    border-radius: 16px !important;
    background: linear-gradient(90deg, #0369a1, #0891b2) !important;
    color: #f0f9ff !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    border: 1px solid rgba(56,189,248,0.3) !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 24px rgba(8,145,178,0.25) !important;
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
    padding: 28px 22px;
    text-align: center;
    font-family: 'Inter', sans-serif;
    transition: all 0.3s ease;
    min-height: 220px;
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
    font-family: 'Orbitron', monospace;
    font-size: 13px;
    font-weight: 700;
    color: #e2e8f0;
    letter-spacing: 1px;
    margin-bottom: 10px;
    text-transform: uppercase;
}

.feature-card p {
    font-size: 13px;
    color: #64748b;
    line-height: 1.6;
    margin: 0;
}

/* ── RESULT CARD ── */
.result-fake {
    padding: 22px 28px;
    border-radius: 18px;
    text-align: center;
    margin-top: 24px;
    font-family: 'Orbitron', monospace;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 1px;
    background: rgba(239, 68, 68, 0.08);
    border: 1.5px solid rgba(239,68,68,0.35);
    color: #f87171;
    box-shadow: 0 0 30px rgba(239,68,68,0.12), inset 0 0 30px rgba(239,68,68,0.03);
    animation: resultPop 0.4s cubic-bezier(0.16,1,0.3,1);
}

.result-real {
    padding: 22px 28px;
    border-radius: 18px;
    text-align: center;
    margin-top: 24px;
    font-family: 'Orbitron', monospace;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 1px;
    background: rgba(16, 185, 129, 0.08);
    border: 1.5px solid rgba(16,185,129,0.35);
    color: #34d399;
    box-shadow: 0 0 30px rgba(16,185,129,0.12), inset 0 0 30px rgba(16,185,129,0.03);
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
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 8px;
}

.metric-value {
    font-family: 'Orbitron', monospace;
    font-size: 32px;
    font-weight: 900;
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
    color: #94a3b8;
    line-height: 1.5;
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
    font-size: 14px;
    color: #e2e8f0;
    font-weight: 500;
}

.settings-sub {
    font-size: 12px;
    color: #475569;
    margin-top: 2px;
}

.badge-on {
    background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.3);
    color: #34d399;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    font-family: 'Orbitron', monospace;
    letter-spacing: 0.5px;
}

/* ── FOOTER ── */
.footer {
    text-align: center;
    color: #1e293b;
    font-size: 12px;
    margin-top: 60px;
    padding-bottom: 40px;
    font-family: 'Inter', sans-serif;
    letter-spacing: 1px;
    text-transform: uppercase;
}

/* ── TABS ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(14,26,50,0.5);
    padding: 6px;
    border-radius: 16px;
    border: 1px solid rgba(56,189,248,0.1);
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 12px;
    padding: 10px 22px;
    color: #475569;
    font-family: 'Orbitron', monospace;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    transition: all 0.2s;
}

.stTabs [aria-selected="true"] {
    background: rgba(56,189,248,0.12) !important;
    color: #38bdf8 !important;
    border: 1px solid rgba(56,189,248,0.25) !important;
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
    .main-title { font-size: 36px; }
    .glass-card { padding: 20px 16px; border-radius: 18px; }
    .block-container { padding-left: 0.75rem !important; padding-right: 0.75rem !important; }
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
    "🏠  Home",
    "🔍  Analyze",
    "💡  Tips",
    "⚙️  Settings"
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
                <div style="font-family:'Orbitron',monospace;font-size:36px;font-weight:900;color:{color};margin-bottom:10px;">{num}</div>
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
                data       = vectorizer.transform([job_text])
                prediction = model.predict(data)[0]
                proba      = model.predict_proba(data)[0]
                fake_pct   = proba[1] * 100
                real_pct   = proba[0] * 100

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

            risk_level = "HIGH RISK" if fake_pct >= 70 else "MEDIUM RISK" if fake_pct >= 40 else "LOW RISK"
            risk_color = "#ef4444" if fake_pct >= 70 else "#f59e0b" if fake_pct >= 40 else "#10b981"

            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span style="font-size:13px;color:#475569;font-family:'Inter',sans-serif;">Overall Fraud Risk</span>
                <span style="font-family:'Orbitron',monospace;font-size:13px;font-weight:700;color:{risk_color};">{risk_level}</span>
            </div>
            """, unsafe_allow_html=True)
            st.progress(int(fake_pct))

            st.markdown(f"""
            <div style="margin-top:16px;font-family:'Inter',sans-serif;font-size:13px;color:#475569;line-height:1.7;">
                Model confidence: <span style="color:#e2e8f0;font-weight:600;">{max(fake_pct, real_pct):.1f}%</span> &nbsp;·&nbsp;
                Prediction: <span style="color:{risk_color};font-weight:600;">{'Fraudulent' if prediction == 1 else 'Legitimate'}</span>
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
    <div style="font-family:'Inter',sans-serif;font-size:14px;color:#64748b;line-height:1.8;">
        <b style="color:#e2e8f0;">JobShield AI</b> is a machine learning-powered fake job detection system 
        trained on thousands of real and fraudulent job postings using TF-IDF vectorization 
        and a classification model.<br><br>
        Built to protect job seekers from online fraud, phishing, and financial scams 
        disguised as employment opportunities.<br><br>
        <span style="color:#38bdf8;font-family:'Orbitron',monospace;font-size:12px;">
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