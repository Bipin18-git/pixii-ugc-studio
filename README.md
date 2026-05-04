# Pixii | AI-Powered UGC Video Agent 🎬

Pixii is an autonomous AI agent that converts static product photos into high-converting, 15-30 second UGC (User Generated Content) style videos. Built for small e-commerce brands, it eliminates the need for expensive creators and slow rendering times by leveraging agentic search and context-aware asset matching.

## 🚀 Key Features
- **Visual Intelligence:** Uses Gemini 1.5 Flash Vision to deeply understand product branding and context.
- **Agentic Sourcing:** Dynamically engineers search strategies to find the perfect human-centric lifestyle B-roll.
- **Real-time Delivery:** Fetches high-definition, royalty-free footage via Pexels API in milliseconds.
- **Production UI:** A sleek, fully responsive dashboard built with Streamlit and custom Glassmorphism CSS.

## 🛠️ Architecture Stack
- **Frontend Engine:** Streamlit
- **Vision/Agent Brain:** Google Gemini 1.5 API
- **Asset Pipeline:** Pexels HD Video API
- **Language:** Python 3.10+

## ⚙️ Local Deployment
1. Clone the repository to your machine.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Add your `GEMINI_API_KEY` and `PEXELS_API_KEY` to your `.streamlit/secrets.toml` file.
4. Launch the application: `streamlit run main.py`

---
*Built by Bipin Kumar | Final Year ECE Student @ SMVDU | NPTEL Star*