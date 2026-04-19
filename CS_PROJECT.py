import streamlit as st
import sqlite3

st.title("📱 Smart Phone Recommender System")

# -----------------------------
# 🧠 STEP 1: ASK USER INPUTS
# -----------------------------
ram = st.selectbox("RAM", [None, 4, 6, 8, 12, 16])
storage = st.selectbox("Storage", [None, 64, 128, 256, 512])
battery = st.selectbox("Battery", [None, 4000, 4500, 5000, 6000])
camera = st.selectbox("Camera (MP)", [None, 12, 50, 64, 108, 200])
tag = st.selectbox("Use Case", [None, "gaming", "camera", "budget", "premium"])

# -----------------------------
# 🗄️ STEP 2: QUERY DATABASE
# -----------------------------
def get_phones():
    conn = sqlite3.connect("phones.db")
    cursor = conn.cursor()

    query = "SELECT * FROM phones WHERE 1=1"
    params = []

    if ram:
        query += " AND ram >= ?"
        params.append(ram)

    if storage:
        query += " AND storage >= ?"
        params.append(storage)

    if battery:
        query += " AND battery >= ?"
        params.append(battery)

    if camera:
        query += " AND camera >= ?"
        params.append(camera)

    if tag:
        query += " AND tags LIKE ?"
        params.append(f"%{tag}%")

    cursor.execute(query, params)
    results = cursor.fetchall()

    conn.close()
    return results

# -----------------------------
# 🚀 STEP 3: SHOW RESULTS
# -----------------------------
if st.button("Find Phones"):
    phones = get_phones()

    if phones:
        st.subheader("📱 Matching Phones")

        for p in phones:
            st.markdown(f"""
            ### {p[1]}
            - RAM: {p[2]} GB  
            - Storage: {p[3]} GB  
            - Battery: {p[4]} mAh  
            - Camera: {p[5]} MP  
            - Screen: {p[6]} inch  
            - Tags: {p[7]}
            """)
    else:
        st.warning("No matching phones found. Try relaxing requirements.")
