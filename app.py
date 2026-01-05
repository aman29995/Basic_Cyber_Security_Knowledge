import streamlit as st

from auth import login_user
from rbac import select_role
from database_pg import init_db, save_score
from score_manager import init_score, get_score

# -------------------------------------------------
# BASIC APP CONFIG
# -------------------------------------------------
st.set_page_config(page_title="CyberQuest ENTERPRISE", layout="wide")

# -------------------------------------------------
# INITIAL SETUP
# -------------------------------------------------
init_db()
login_user()
select_role()
init_score()

# -------------------------------------------------
# SESSION STATE INITIALIZATION
# -------------------------------------------------
if "vm_level" not in st.session_state:
    st.session_state.vm_level = 1

if "last_role" not in st.session_state:
    st.session_state.last_role = st.session_state.role

# Reset VM level if role changes
if st.session_state.last_role != st.session_state.role:
    st.session_state.vm_level = 1
    st.session_state.last_role = st.session_state.role

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("🏢 CyberQuest ENTERPRISE – SOC + VM Cyber Range")

st.markdown(f"""
**👤 User:** {st.session_state.user}  
**🧑‍💼 Role:** {st.session_state.role}  
**🏆 Score:** {get_score()}
""")

st.divider()

# -------------------------------------------------
# ROLE-BASED NAVIGATION
# -------------------------------------------------
if st.session_state.role == "SOC Analyst":
    menu = st.sidebar.radio(
        "SOC Menu",
        ["🎮 SOC Games", "📊 SOC Summary"],
        key="soc_menu"
    )

elif st.session_state.role == "VM Lead":
    menu = st.sidebar.radio(
        "VM Menu",
        ["🛡️ VM Games", "📊 VM Dashboard"],
        key="vm_menu"
    )

# =================================================
# SOC ANALYST GAME (SINGLE INCIDENT – CLEAN)
# =================================================
if st.session_state.role == "SOC Analyst":

    if menu == "🎮 SOC Games":
        st.subheader("🚨 SOC Incident Simulation")

        st.write("""
        🚨 **Alert:** Employee clicked a suspicious phishing email.
        """)

        action = st.selectbox(
            "Choose your response:",
            ["Ignore", "Reset password", "Disable account"],
            key="soc_action"
        )

        if st.button("Respond to Incident", key="soc_respond"):
            if action == "Reset password":
                st.success("Correct SOC response!")
                st.session_state.score += 20
                save_score(st.session_state.user, st.session_state.score)
            else:
                st.error("Incident escalated due to wrong action.")

    elif menu == "📊 SOC Summary":
        st.subheader("📊 SOC Performance Summary")
        st.metric("Total Score", get_score())

# =================================================
# VM LEAD – MULTI-LEVEL GAME (INDUSTRY FLOW)
# =================================================
if st.session_state.role == "VM Lead":

    if menu == "🛡️ VM Games":

        # ---------------- LEVEL 1 ----------------
        if st.session_state.vm_level == 1:
            st.subheader("🛡️ VM Level 1 – Vulnerability Prioritization")

            st.write("""
            🔎 Scan Results:
            - CVSS 9.8 (Critical)
            - CVSS 7.5 (High)
            - CVSS 5.0 (Medium)
            """)

            action = st.radio(
                "Which vulnerability do you remediate first?",
                ["CVSS 5.0", "CVSS 7.5", "CVSS 9.8"],
                key="vm_lvl1"
            )

            if st.button("Proceed", key="vm_btn1"):
                if action == "CVSS 9.8":
                    st.success("Correct! Critical risk addressed.")
                    st.session_state.score += 20
                    st.session_state.vm_level = 2
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.error("Critical vulnerability left unpatched.")

        # ---------------- LEVEL 2 ----------------
        elif st.session_state.vm_level == 2:
            st.subheader("🛡️ VM Level 2 – Exploitable Vulnerability")

            st.write("""
            🚨 Threat intel confirms **active exploitation**.
            """)

            action = st.radio(
                "Your response?",
                ["Emergency patch", "Wait for maintenance window", "Accept risk"],
                key="vm_lvl2"
            )

            if st.button("Mitigate", key="vm_btn2"):
                if action == "Emergency patch":
                    st.success("Exploit blocked successfully.")
                    st.session_state.score += 25
                    st.session_state.vm_level = 3
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.error("System compromise detected.")

        # ---------------- LEVEL 3 ----------------
        elif st.session_state.vm_level == 3:
            st.subheader("🛡️ VM Level 3 – Business Impact Decision")

            st.write("""
            ⚠️ Patch may cause downtime. Business is concerned.
            """)

            action = st.radio(
                "Decision?",
                ["Patch with approval", "Temporary mitigation", "Accept risk"],
                key="vm_lvl3"
            )

            if st.button("Decide", key="vm_btn3"):
                if action == "Temporary mitigation":
                    st.success("Risk reduced with minimal impact.")
                    st.session_state.score += 20
                    st.session_state.vm_level = 4
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.warning("Decision increases risk.")

        # ---------------- LEVEL 4 ----------------
        elif st.session_state.vm_level == 4:
            st.subheader("🛡️ VM Level 4 – SLA Compliance")

            st.write("""
            📄 SLA requires fixing critical issues within **7 days**.
            """)

            action = st.radio(
                "SLA status?",
                ["Yes – fixed in time", "No – delayed"],
                key="vm_lvl4"
            )

            if st.button("Submit SLA", key="vm_btn4"):
                if action == "Yes – fixed in time":
                    st.success("SLA met successfully.")
                    st.session_state.score += 15
                    st.session_state.vm_level = 5
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.error("SLA breach reported.")

        # ---------------- LEVEL 5 ----------------
        elif st.session_state.vm_level == 5:
            st.subheader("🏁 VM Level 5 – Executive Reporting")

            st.write("""
            📊 Prepare VM report for leadership.
            """)

            action = st.radio(
                "Which metric do you highlight?",
                ["Total vulnerabilities", "Risk reduction & SLA", "Scan count"],
                key="vm_lvl5"
            )

            if st.button("Submit Report", key="vm_btn5"):
                if action == "Risk reduction & SLA":
                    st.success("Executive-ready report delivered.")
                    st.session_state.score += 30
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.warning("Metrics lack business context.")

                st.balloons()
                st.success("🎉 VM Program Comple
