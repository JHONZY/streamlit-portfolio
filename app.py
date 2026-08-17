import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# ----------------------------
# PAGE CONFIGURATION
# ----------------------------
st.set_page_config(
    page_title="JL Borromeo - Automation Portfolio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# LOAD EXTERNAL CSS
# ----------------------------
def load_css():
    try:
        with open("assets/style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown(
            """
            <style>
                .main-title { font-size: 2.5rem; font-weight: bold; color: #1E88E5; }
                .section-header { font-size: 1.8rem; font-weight: 600; border-bottom: 2px solid #1E88E5; }
                .skill-tag { background: #E3F2FD; border-radius: 20px; padding: 0.3rem 0.8rem; display: inline-block; }
                .project-card { background: #F8F9FA; border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem; }
                .footer { text-align: center; color: #888; margin-top: 3rem; }
            </style>
            """,
            unsafe_allow_html=True
        )

load_css()



col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<h2 class="main-title">👋 Hi, I’m JL Borromeo</h2>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Automation Developer · Problem Solver · Workflow Optimizer</p>', unsafe_allow_html=True)
    st.write("""
    I turn **repetitive, time‑consuming tasks** into automated, efficient processes. 
    Whether it’s daily reports, data entry, file organisation, or email campaigns – 
    I build tools that let you focus on what truly matters.
    """)
    st.markdown("📍 Based in Rodriguez Rizal | &#128241; 09055217805")
with col2:
    st.image("images/profile.png", width=250, caption="")
# About Me
st.markdown('<p class="section-header">🧑‍💻 About Me</p>', unsafe_allow_html=True)
st.markdown("""
I’m a **Python Developer with 3+ years of experience** specialising in building automation 
solutions that eliminate redundant and repetitive tasks. I analyse workflows, identify 
inefficiencies, and develop scripts or full‑fledged applications that save teams hours every day.  
<br><br>
**My superpower:** I can take a messy, repetitive task and turn it into a one‑click operation.
""", unsafe_allow_html=True)
# Skills
st.markdown('<p class="section-header">🔧 Core Skills</p>', unsafe_allow_html=True)
skills = [
    "Python", "Streamlit", "Pandas", "Web Scraping (BeautifulSoup, Selenium)",
    "API Integration", "Automation Scripting", "Task Scheduling", "Excel/CSV Automation",
    "Email Automation", "File System Management", "Workflow Optimisation",
    "SQL / Database Management"  # added to reflect new CRUD skill
]
cols = st.columns(4)
for i, skill in enumerate(skills):
    cols[i % 4].markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
# Projects (removed Email Sender, added Data Manager project)
st.markdown('<p class="section-header">📌 Featured Projects</p>', unsafe_allow_html=True)
st.markdown("""
<div class="project-card">
    <h4>📊 Automated Daily Reporting System</h4>
    <p>Built a pipeline that extracts data from multiple sources (databases, APIs, spreadsheets), 
    processes it, and delivers a polished PDF/Excel report to stakeholders every morning – 
    completely hands‑off.</p>
    <p><strong>Tech:</strong> Python, Pandas, SQLite, SMTP, APScheduler</p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="project-card">
    <h4>📁 Smart File Organiser</h4>
    <p>Developed a tool that monitors a download folder and automatically sorts incoming files 
    into category folders (images, documents, archives) based on extension and content type.</p>
    <p><strong>Tech:</strong> Python, Watchdog, shutil, Pathlib</p>
</div>
""", unsafe_allow_html=True)
# New project showcasing the Data Manager
st.markdown("""
<div class="project-card">
    <h4>📋 Interactive Data Manager with Dashboard</h4>
    <p>Built a full‑fledged CRUD application with an SQLite backend, allowing users to add, 
    edit, delete, and visualise task data. Includes a real‑time dashboard with charts for 
    status distribution – all within a Streamlit interface.</p>
    <p><strong>Tech:</strong> Python, Streamlit, SQLite, Pandas, Altair</p>
</div>
""", unsafe_allow_html=True)
# What I Can Automate
st.markdown('<p class="section-header">⚡ What I Can Automate</p>', unsafe_allow_html=True)
st.write("""
- **Daily / Weekly Reports** – pull data from multiple sources, generate charts, and email summaries.
- **Data Entry & Cleanup** – transform messy Excel/CSV files, remove duplicates, fill missing values.
- **Email Campaigns** – send personalised bulk emails with attachments and tracking.
- **File Management** – organise, rename, backup, or archive files based on rules.
- **Web Data Extraction** – scrape product prices, news headlines, or job listings.
- **Task Scheduling** – set up cron‑like jobs to run your scripts automatically.
- **And much more** – bring me your repetitive task, and I’ll solve it.
""")
# Contact
st.markdown('<p class="section-header">📬 Let’s Connect</p>', unsafe_allow_html=True)
st.write("""
I’m always open to discussing new opportunities, freelance projects, or just chatting about automation.
Reach out, and let’s make your workflows smarter!
""")
col1, col2, col3 = st.columns(3)
with col1:
    # Email - direct Gmail compose
    st.markdown(
        '<a href="https://mail.google.com/mail/?view=cm&fs=1&to=jhonlester0111@gmail.com" target="_blank" class="custom-button" style="display:block; text-align:center; padding:0.5rem; background-color:#FF4B4B; color:white; border-radius:0.5rem; text-decoration:none; font-weight:bold;">📧 Email Me</a>',
        unsafe_allow_html=True
    )
with col2:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/john-lester-borromeo-694447253/", use_container_width=True)
with col3:
    st.link_button("🐙 GitHub", "https://github.com/JHONZY", use_container_width=True)
st.markdown('<p class="footer">&copy; 2026 JL Borromeo · Built with Streamlit ❤️</p>', unsafe_allow_html=True)
# ---------------------------
# ROUTING
# ---------------------------
