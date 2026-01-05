
import streamlit as st

def select_role():
    if "role" not in st.session_state:
        st.session_state.role = None
    if not st.session_state.role:
        role = st.radio("Select Role", ["SOC Analyst", "VM Lead"])
        if st.button("Continue"):
            st.session_state.role = role
            st.experimental_rerun()
        st.stop()
