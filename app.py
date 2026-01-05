import streamlit as st
from auth import login_user
from rbac import select_role
from database_pg import init_db, save_score
from score_manager import init_score, get_score

# ---- INIT ----
st.set_page_config(page_title="CyberQuest ENTERPRISE", layout="wide")

init_db()
login_user()
select_role()
init_score()

st.title("🏢 CyberQuest ENTERPRISE – Cyber Range")

st.markdown(f"""
**User:** {st.session_state.user}  
**Role:** {st.session_state.role}  
**Score:** {get_score()}
""")

st.divider()

# ---- ROLE BASED MENU ----
if st.session_state.role == "SOC Analyst":
    menu = st.sidebar.radio(
        "SOC Menu",
        ["🎮 SOC Games", "📊 SOC Summary"]
    )

elif st.session_state.role == "VM Lead":
    menu = st.sidebar.radio(
        "VM Menu",
        ["🛡️ VM Games", "📊 VM Dashboard"]
    )

# ---- SOC GAME FLOW ----
if st.session_state.role == "SOC Analyst":

    if menu == "🎮 SOC Games":
        st.subheader("🚨 SOC Incident Simulation")

        st.write("""
        🚨 ALERT: Phishing email reported by employee.
        """)

        action = st.selectbox(
            "Choose your response:",
            ["Ignore", "Reset password", "Disable account"]
        )

        if st.button("Respond to Incident"):
            if action == "Reset password":
                st.success("Correct SOC response!")
                st.session_state.score += 20
                save_score(st.session_state.user, st.session_state.score)
            else:
                st.error("Incident escalated.")

    elif menu == "📊 SOC Summary":
        st.subheader("SOC Performance Summary")
        st.metric("Total Score", get_score())

# ---- VM GAME FLOW ----
if st.session_state.role == "VM Lead":

    if menu == "🛡️ VM Games":
        st.subheader("🛡️ Vulnerability Management Simulation")

        st.write("""
        🔎 Scan Result:
        - CVSS 9.8 (Critical)
        - CVSS 7.5 (High)
        - CVSS 5.0 (Medium)
        """)

        action = st.radio(
            "Which vulnerability do you remediate first?",
            ["CVSS 5.0", "CVSS 7.5", "CVSS 9.8"]
        )

        if st.button("Apply Remediation"):
            if action == "CVSS 9.8":
                st.success("Correct VM prioritization!")
                st.session_state.score += 25
                save_score(st.session_state.user, st.session_state.score)
            else:
                st.warning("High risk left unpatched.")

    elif menu == "📊 VM Dashboard":
        st.subheader("VM Lead Dashboard")
        st.metric("Risk Reduction Score", get_score())
