import streamlit as st
import pandas as pd

# Judul & intro
st.markdown("# 📱 Sistem Rekomendasi Handphone")
st.markdown("Selamat datang! Pilih budget dan kebutuhanmu, lalu dapatkan rekomendasi HP yang cocok.")


# Layout input & output
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔍 Input")
    budget = st.selectbox("Pilih Budget Anda:", ["< 3 juta", "3-6 juta", "> 6 juta"])
    kebutuhan = st.selectbox("Pilih Kebutuhan:", ["Gaming", "Fotografi", "Harian", "Prestige"])
    if st.button("Dapatkan Rekomendasi"):
        st.session_state['hasil'] = (budget, kebutuhan)

with col2:
    st.subheader("📊 Rekomendasi")
    if 'hasil' in st.session_state:
        b, k = st.session_state['hasil']
        if b == "< 3 juta" and k == "Harian":
            st.success("Xiaomi Redmi Note atau Oppo A series")
        elif b == "3-6 juta" and k == "Gaming":
            st.success("Samsung Galaxy A series atau Xiaomi Poco")
        elif b == "> 6 juta" and k == "Fotografi":
            st.success("Samsung Galaxy S series atau iPhone 13")
        elif b == "> 6 juta" and k == "Prestige":
            st.success("iPhone 14 Pro atau Samsung Galaxy Z Flip")
        else:
            st.warning("Belum ada rekomendasi untuk kombinasi ini.")

# Tabel perbandingan
st.markdown("## 📋 Perbandingan Brand")
data = {
    "Brand": ["Samsung", "Xiaomi", "Oppo", "iPhone"],
    "Kelebihan": ["Layar & kamera bagus", "Harga terjangkau", "Kamera selfie oke", "Prestige & ekosistem"],
    "Range Harga": ["3-15 juta", "2-8 juta", "2-7 juta", "10-20 juta"]
}
df = pd.DataFrame(data)
st.table(df)