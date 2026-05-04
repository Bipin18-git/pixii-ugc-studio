import streamlit as st
import google.generativeai as genai
from PIL import Image
import requests
import time

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="Pixii | AI UGC Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. Ultra-Aggressive Professional UI (Dark Glassmorphism) ---
st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(at 0% 0%, hsla(253,16%,7%,1) 0, transparent 50%), 
                        radial-gradient(at 50% 0%, hsla(225,39%,30%,1) 0, transparent 50%), 
                        radial-gradient(at 100% 0%, hsla(339,49%,30%,1) 0, transparent 50%);
            background-color: #0f172a;
            color: #f8fafc;
        }
        [data-testid="stFileUploader"] section {
            background-color: rgba(255, 255, 255, 0.03) !important;
            border: 1px dashed rgba(129, 140, 248, 0.4) !important;
            border-radius: 16px !important;
            color: #94a3b8 !important;
        }
        [data-testid="stFileUploader"] section:hover {
            border-color: #818cf8 !important;
            background-color: rgba(129, 140, 248, 0.05) !important;
        }
        [data-testid="stFileUploadDropzone"] { background-color: transparent !important; }
        
        div[data-baseweb="select"] > div {
            background-color: rgba(255, 255, 255, 0.03) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            color: white !important;
            border-radius: 12px !important;
        }
        
        .main-container { max-width: 1100px; margin: auto; padding: 1rem; }
        .hero-title {
            font-size: clamp(2.5rem, 6vw, 4.5rem);
            font-weight: 800;
            background: linear-gradient(to right, #818cf8, #c084fc, #fb7185);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            line-height: 1.1;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .hero-subtitle {
            text-align: center;
            color: #94a3b8;
            font-size: 1.1rem;
            margin-bottom: 3rem;
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 28px;
            padding: 2.5rem;
            height: 100%;
        }
        
        .stButton>button {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            color: white !important;
            border: none !important;
            padding: 1rem !important;
            border-radius: 14px !important;
            font-weight: 700 !important;
            width: 100% !important;
            box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4) !important;
        }
        
        footer {visibility: hidden;}
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 3. UI Header ---
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("### 🎬 Pixii <span style='color:#818cf8; font-size:0.8rem; font-weight:bold;'>STUDIO v1.0</span>", unsafe_allow_html=True)

# --- 4. Hero Section ---
st.markdown("<div class='hero-title'>UGC Video Agent</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>The autonomous pipeline that turns raw product photos into viral-ready video ads instantly.</div>", unsafe_allow_html=True)

# --- 5. Main Dashboard ---
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<div class='glass-card'><h3>📸 1. Source Asset</h3><p style='color:#64748b; font-size:0.9rem;'>Upload a high-quality product photo.</p>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], label_visibility="collapsed")
    if uploaded_file:
        st.image(uploaded_file, use_container_width=True, caption="Source Preview")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='glass-card'><h3>🤖 2. Logic Engine</h3><p style='color:#64748b; font-size:0.9rem;'>Configure the agent's directorial style.</p>", unsafe_allow_html=True)
    audience = st.selectbox("Strategic Optimization", ["TikTok Viral Hook", "Instagram Reels Aesthetic", "High-Conversion FB Ad"])
    generate_btn = st.button("🚀 EXECUTE PIPELINE")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. The Autonomous Pipeline ---
if generate_btn:
    if not uploaded_file:
        st.warning("Please provide a product asset first.")
    else:
        st.markdown("<hr style='opacity:0.1'>", unsafe_allow_html=True)
        
        try:
            # SECURE KEYS FETCH
            GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
            PEXELS_API_KEY = st.secrets["PEXELS_API_KEY"]
            
            with st.status("🧠 Agent is processing...", expanded=True) as status:
                st.write("🔍 Running Computer Vision Analysis...")
                genai.configure(api_key=GEMINI_API_KEY)
                vision_model = genai.GenerativeModel('gemini-1.5-flash')
                
                img = Image.open(uploaded_file)
                details = vision_model.generate_content(["Identify this product and its core benefit in one short sentence. Strictly no brand names.", img]).text.strip()
                st.write(f"**Insight:** {details}")
                
                st.write("📡 Generating B-Roll sourcing strategy...")
                query = vision_model.generate_content(f"Based on '{details}', provide exactly 3 keywords to find a lifestyle vertical video of a person using it. Words only. No punctuation.").text.strip().replace('"', '').replace("'", "")
                
                st.write(f"🎥 Fetching HD assets for: '{query}'...")
                res = requests.get(f"https://api.pexels.com/videos/search?query={query}&orientation=portrait&per_page=1", headers={"Authorization": PEXELS_API_KEY}).json()
                
                if res.get('videos'):
                    video_url = res['videos'][0]['video_files'][0]['link']
                    status.update(label="UGC Rendering Complete!", state="complete", expanded=False)
                    
                    st.markdown(f"""
                        <div style="background: rgba(129, 140, 248, 0.05); padding: 1.5rem; border-radius: 20px; border-left: 4px solid #818cf8; margin: 2rem 0;">
                            <h4 style="margin:0; color:#818cf8;">✅ Final Production Asset</h4>
                            <p style="margin:0; color:#94a3b8; font-size:0.9rem;">Analysis: {details}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.video(video_url)
                    st.balloons()
                else:
                    st.error("No high-quality asset match found. Try a different product photo.")
        except Exception as e:
            # 👉 Naya Error Checker 👈
            st.error(f"🚨 Asli Error ye hai: {e}")

st.markdown("</div>", unsafe_allow_html=True)
