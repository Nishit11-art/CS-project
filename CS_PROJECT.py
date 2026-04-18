import streamlit as st

def understand(text):
    text = text.lower()

    ram, storage, battery = 4, 64, 4000

    if "gaming" in text:
        ram = 8
        storage = 128
        battery = 5000

    if "intense gaming" in text:
        ram = 12
        storage = 256
        battery = 6000

    return ram, storage, battery


st.title("📱 Phone Recommender AI")

user_input = st.text_input("What do you need the phone for?")

if user_input:
    ram, storage, battery = understand(user_input)

    st.write("### Recommended Specs:")
    st.write(f"RAM: {ram} GB")
    st.write(f"Storage: {storage} GB")
    st.write(f"Battery: {battery} mAh")
    
