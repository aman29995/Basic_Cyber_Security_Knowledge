import streamlit as st
from .helpers import add_score, sla_timer, mitre_hint

def soc_level_1(mode):
    st.subheader("SOC Level 1 – Phishing Detection")
    if mode == "Fresher":
        mitre_hint("T1566", "Phishing", "Email-based initial access")
    if mode == "Advanced":
        if sla_timer(60) == 0:
            st.session_state.soc_level += 1
            return
    if st.button("Analyze Email"):
        add_score(10)
        st.session_state.soc_level += 1

def soc_level_2(mode):
    st.subheader("SOC Level 2 – Containment")
    if st.button("Reset Credentials"):
        add_score(20)
        st.session_state.soc_level += 1

def soc_level_3(mode):
    st.subheader("SOC Level 3 – Handover")
    if st.button("Hand-off to VM"):
        add_score(30)
        st.session_state.soc_completed = True
        st.session_state.soc_level += 1