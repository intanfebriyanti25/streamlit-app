import streamlit as st
import joblib

st.title("Aplikasi Machine Learning Pertamaku")

nama = st.text_input("Masukkan nama:")
umur = st.number_input("Masukkan umur:", 0, 100)
teks = st.text_area("Masukkan teks ulasan", height=150)
pilihan = st.selectbox("Pilih model:", ["KNN", "SVM", "Random Forest"])

if st.button("Prediksi"):
    if teks.strip() == "":
        st.warning("Teks tidak boleh kosong")
    elif len(teks) > 1000:
        st.error("Teks terlalu panjang")
    else:
        st.success("Prediksi berhasil dijalankan!")