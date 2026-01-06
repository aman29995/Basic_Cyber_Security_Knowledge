import streamlit as st
from .helpers import add_score, sla_timer, mitre_hint

def vm_level_1(mode):
    st.subheader("VM Level 1 – Emergency Patch")
    if st.button("Deploy Patch"):
        add_score(20)
        st.session_state.vm_level += 1

def vm_level_2(mode):
    st.subheader("VM Level 2 – Risk Mitigation")
    if st.button("Temporary Mitigation"):
        add_score(20)
        st.session_state.vm_level += 1

def vm_level_3(mode):
    st.subheader("VM Level 3 – Executive Report")
    if st.button("Submit Report"):
        add_score(30)
        st.session_state.vm_completed = True
        st.balloons()