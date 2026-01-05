
import streamlit as st

def login_user():
    if "user" not in st.session_state:
        st.session_state.user = None
    if not st.session_state.user:
        st.title("Login")
        u = st.text_input("Username")
        if st.button("Login"):
            st.session_state.user = u
            st.experimental_rerun()
        st.stop()
