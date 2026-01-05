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
# ---- VM GAME FLOW (MULTI-LEVEL) ----
if st.session_state.role == "VM Lead":

    if menu == "🛡️ VM Games":

        # ---------------- VM LEVEL 1 ----------------
        if st.session_state.vm_level == 1:
            st.subheader("🛡️ VM Level 1 – Vulnerability Discovery")

            st.write("""
            🔎 Scan completed on new assets.
            Vulnerabilities identified with different severities.
            """)

            action = st.radio(
                "Which vulnerability do you remediate first?",
                ["CVSS 5.0", "CVSS 7.5", "CVSS 9.8"]
            )

            if st.button("Proceed"):
                if action == "CVSS 9.8":
                    st.success("Correct! Critical risk prioritized.")
                    st.session_state.score += 20
                    st.session_state.vm_level = 2
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.error("High risk vulnerability left exposed.")

        # ---------------- VM LEVEL 2 ----------------
        elif st.session_state.vm_level == 2:
            st.subheader("🛡️ VM Level 2 – Exploitable Vulnerability")

            st.write("""
            🚨 Threat intelligence reports active exploitation
            for a CVSS 9.8 vulnerability.
            """)

            action = st.radio(
                "What is your response?",
                ["Emergency patch", "Wait for maintenance window", "Accept risk"]
            )

            if st.button("Mitigate"):
                if action == "Emergency patch":
                    st.success("Exploit path blocked.")
                    st.session_state.score += 25
                    st.session_state.vm_level = 3
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.error("System compromise detected.")

        # ---------------- VM LEVEL 3 ----------------
        elif st.session_state.vm_level == 3:
            st.subheader("🛡️ VM Level 3 – Patch vs Business Impact")

            st.write("""
            ⚠️ Business team warns patch may cause downtime.
            """)

            action = st.radio(
                "Decision?",
                ["Patch with approval", "Temporary mitigation", "Accept risk"]
            )

            if st.button("Decide"):
                if action == "Temporary mitigation":
                    st.success("Risk reduced with minimal impact.")
                    st.session_state.score += 20
                    st.session_state.vm_level = 4
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.warning("Decision may increase risk.")

        # ---------------- VM LEVEL 4 ----------------
        elif st.session_state.vm_level == 4:
            st.subheader("🛡️ VM Level 4 – SLA & Compliance")

            st.write("""
            📄 SLA requires critical vulnerabilities
            to be fixed within 7 days.
            """)

            action = st.radio(
                "Are you SLA compliant?",
                ["Yes – fixed in time", "No – delayed"]
            )

            if st.button("Submit SLA Status"):
                if action == "Yes – fixed in time":
                    st.success("SLA met.")
                    st.session_state.score += 15
                    st.session_state.vm_level = 5
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.error("SLA breach reported.")

        # ---------------- VM LEVEL 5 ----------------
        elif st.session_state.vm_level == 5:
            st.subheader("🏁 VM Level 5 – Executive Reporting")

            st.write("""
            📊 Prepare executive VM report.
            """)

            action = st.radio(
                "Which metric do you highlight?",
                ["Total vulnerabilities", "Risk reduction & SLA", "Scan count"]
            )

            if st.button("Submit Report"):
                if action == "Risk reduction & SLA":
                    st.success("Leadership-ready report delivered.")
                    st.session_state.score += 30
                    save_score(st.session_state.user, st.session_state.score)
                else:
                    st.warning("Metrics lack business context.")

                st.balloons()
                st.success("🎉 VM Program Completed!")
