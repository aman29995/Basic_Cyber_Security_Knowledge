# score_manager.py
import streamlit as st

def init_score():
    if "score" not in st.session_state:
        st.session_state.score = 0

def get_score():
    return st.session_state.score
