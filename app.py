
import streamlit as st
from auth import login_user
from rbac import select_role
from database_pg import init_db, save_score, load_leaderboard

st.set_page_config(page_title="CyberQuest ENTERPRISE", layout="wide")

init_db()
login_user()
select_role()

st.title("🏢 CyberQuest ENTERPRISE – SOC + VM Cyber Range")

st.write(f"User: {st.session_state.user}")
st.write(f"Role: {st.session_state.role}")

if "score" not in st.session_state:
    st.session_state.score = 0

if st.button("Simulate Action (+10)"):
    st.session_state.score += 10
    save_score(st.session_state.user, st.session_state.score)

st.metric("Score", st.session_state.score)

st.subheader("🏆 Leaderboard")
data = load_leaderboard()
for u, s in data:
    st.write(f"{u} : {s}")
