# 🛡️ AI Cybersecurity Assistant

An AI-powered cybersecurity application built using Python and Streamlit.

## 📌 Project Overview

The AI Cybersecurity Assistant is a defensive cybersecurity application that helps users understand cybersecurity threats and perform basic security analysis.

The application combines AI-based assistance with rule-based security analysis to provide a simple and beginner-friendly cybersecurity tool.

## 🚀 Features

### 🤖 AI Security Assistant
- Ask cybersecurity-related questions.
- Get AI-generated security explanations.
- Provides risks, security measures, and prevention tips.

### 🚨 Threat Analysis
- Displays common cybersecurity threats.
- Shows risk levels and detected cases.
- Provides threat statistics using charts.

### 📊 Security Dashboard
- Displays total threats.
- Shows high-risk and critical threats.
- Displays overall security status.

### 🔎 URL / Phishing Analyzer
- Analyzes URLs for suspicious indicators.
- Checks HTTPS usage.
- Detects long URLs.
- Detects suspicious symbols.
- Detects suspicious words.
- Calculates a risk score and risk level.

### 📋 Security Log Analyzer
- Analyzes security log text.
- Detects failed login attempts.
- Detects suspicious IP activity.
- Detects high-risk events.
- Calculates the overall risk level.

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Pandas
- Plotly
- Python-dotenv
- Scikit-learn
- Requests
- Pydantic
- Scapy

## 📁 Project Structure

```text
my project/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── modules/
    ├── __init__.py
    ├── ai_assistant.py
    ├── url_analyzer.py
    └── log_analyzer.py