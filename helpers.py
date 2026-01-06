import streamlit as st
import time

def init_state(key, value):
    if key not in st.session_state:
        st.session_state[key] = value

def add_score(points):
    st.session_state.score += points

def sla_timer(seconds):
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = time.time()
    remaining = seconds - int(time.time() - st.session_state.timer_start)
    if remaining <= 0:
        st.error("SLA Breached")
        return 0
    st.warning(f"Time Remaining: {remaining}s")
    return remaining

def mitre_hint(tech_id, name, desc):
    with st.expander(f"MITRE {tech_id} – {name}"):
        st.write(desc)