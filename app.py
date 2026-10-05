import os
import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
from google import genai
from modules.url_analyzer import analyze_url
from modules.log_analyzer import analyze_logs
# -----------------------------
# Load API Key
# -----------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY not found in .env file")
    st.stop()

client = genai.Client(api_key=API_KEY)


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Cybersecurity Assistant",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Cybersecurity Assistant")
st.write("AI-powered cybersecurity analysis tool")


# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🔐 Security Tools")

option = st.sidebar.radio(
    "Choose a feature:",
    [
        "AI Security Assistant",
        "Threat Analysis",
        "Security Dashboard",
        "URL / Phishing Analyzer",
        "Security Log Analyzer",
    ]
)


# ==================================================
# AI SECURITY ASSISTANT
# ==================================================

if option == "AI Security Assistant":

    st.header("🤖 AI Security Assistant")

    question = st.text_area(
        "Ask your cybersecurity question:",
        placeholder="Example: What is phishing and how can I prevent it?"
    )

    if st.button("Analyze 🔍"):

        if question.strip() == "":
            st.warning("Please enter a cybersecurity question.")

        else:

            prompt = f"""
You are an AI Cybersecurity Assistant.

Answer the user's cybersecurity question in a simple,
clear and beginner-friendly way.

User Question:
{question}

Include:
1. Meaning of the issue
2. Possible risks
3. Security measures
4. Prevention tips

Do not provide instructions for illegal hacking,
malware creation, credential theft, or unauthorized access.
"""

            try:

                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )

                st.subheader("🛡️ Security Analysis")

                if response.text:
                    st.write(response.text)
                else:
                    st.warning("No response received from Gemini.")

            except Exception as e:

                st.error("Gemini request failed.")

                st.code(str(e))


# ==================================================
# THREAT ANALYSIS
# ==================================================

elif option == "Threat Analysis":

    st.header("🚨 Threat Analysis")

    data = {
        "Threat": [
            "Phishing",
            "Malware",
            "Ransomware",
            "DDoS",
            "Credential Attack"
        ],
        "Risk Level": [
            "High",
            "High",
            "Critical",
            "Medium",
            "High"
        ],
        "Detected Cases": [
            85,
            60,
            40,
            30,
            70
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

    st.subheader("📊 Threat Statistics")

    chart = px.bar(
        df,
        x="Threat",
        y="Detected Cases",
        title="Cybersecurity Threat Detection"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


# ==================================================
# SECURITY DASHBOARD
# ==================================================

elif option == "Security Dashboard":

    st.header("📊 Security Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Threats", "285")
    col2.metric("High Risk", "175")
    col3.metric("Critical", "40")
    col4.metric("Protected", "92%")

    st.subheader("🔐 Security Status")

    status = pd.DataFrame({
        "Status": ["Protected", "At Risk"],
        "Count": [92, 8]
    })

    chart = px.pie(
        status,
        names="Status",
        values="Count",
        title="Security Status"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    st.success(
        "Security monitoring system is active."
    )

    st.success(
        "Security monitoring system is active."
    )


# ==================================================
# URL / PHISHING ANALYZER
# ==================================================

elif option == "URL / Phishing Analyzer":

    st.header("🔎 URL / Phishing Analyzer")

    url = st.text_input(
        "Enter a URL to analyze:",
        placeholder="Example: https://www.google.com"
    )

    if st.button("Analyze URL 🔍"):

        if url.strip() == "":
            st.warning("Please enter a URL.")

        else:

            result = analyze_url(url)

            st.subheader("🛡️ Analysis Result")

            st.write("**URL:**", result["url"])
            st.write("**Risk Score:**", result["risk_score"])
            st.write("**Risk Level:**", result["risk_level"])

            st.write("### 🔍 Security Indicators")

            st.write(
                "HTTPS:",
                "✅ Yes" if result["https"] else "❌ No"
            )

            st.write(
                "Long URL:",
                "⚠️ Yes" if result["long_url"] else "✅ No"
            )

            st.write(
                "Suspicious Symbols:",
                "⚠️ Yes" if result["suspicious_symbols"] else "✅ No"
            )

            st.write(
                "Suspicious Words:",
                "⚠️ Yes" if result["suspicious_words"] else "✅ No"
            )

# ==================================================
# SECURITY LOG ANALYZER
# ==================================================

elif option == "Security Log Analyzer":

    st.header("📋 Security Log Analyzer")

    log_text = st.text_area(
        "Paste security logs here:",
        placeholder="Example:\nLogin failed from user\nSuspicious IP detected\nCritical security event",
        height=200
    )

    if st.button("Analyze Logs 🔍"):

        if log_text.strip() == "":
            st.warning("Please enter security logs.")

        else:

            result = analyze_logs(log_text)

            st.subheader("🛡️ Log Analysis Result")

            st.write("**Total Logs:**", result["total_logs"])
            st.write("**Failed Logins:**", result["failed_logins"])
            st.write("**Suspicious IPs:**", result["suspicious_ips"])
            st.write("**High-Risk Events:**", result["high_risk_events"])
            st.write("**Risk Level:**", result["risk_level"])