import streamlit as st
import joblib
from groq import Groq

st.title("Aplikasi Machine Learning Pertamaku")

# ====== BAGIAN FORM PREDIKSI ======
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

st.divider()

# ====== BAGIAN CHATBOT GROQ (LLM) ======
st.subheader("Chatbot dengan Groq LLM")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

prompt = st.text_input("Tanyakan sesuatu ke AI:")

if st.button("Kirim"):
    if prompt.strip() == "":
        st.warning("Pertanyaan tidak boleh kosong")
    else:
        with st.spinner("Sedang memproses jawaban..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
        st.write(response.choices[0].message.content)