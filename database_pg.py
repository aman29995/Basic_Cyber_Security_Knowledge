
import psycopg2
import streamlit as st

def get_conn():
    cfg = st.secrets["postgres_writer"]
    return psycopg2.connect(**cfg)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS scores (username TEXT, score INT)")
    conn.commit()
    conn.close()

def save_score(user, score):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO scores VALUES (%s,%s)", (user, score))
    conn.commit()
    conn.close()

def load_leaderboard():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT username, MAX(score) FROM scores GROUP BY username ORDER BY MAX(score) DESC")
    data = cur.fetchall()
    conn.close()
    return data
