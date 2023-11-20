import streamlit as st

# Aplikasi Streamlit
st.title("Aplikasi Interaktif Sederhana")

# Tambahkan elemen-elemen interaktif
user_input = st.text_input("Masukkan teks:")
st.write("Teks yang dimasukkan:", user_input)
