import streamlit as st
import pandas as pd

st.set_page_config(page_title="Rekomendasi Prodi", layout="wide")

# Header
st.markdown("# 🎓 Sistem Rekomendasi Prodi Informatika")
st.markdown("Temukan prodi yang paling sesuai dengan **minat, bakat, dan potensi kariermu** 🚀")

st.divider()

col1, col2 = st.columns([1, 2])

# INPUT
with col1:
    st.subheader("🔍 Input Data Diri")

    minat = st.selectbox("💡 Minat utama kamu:", [
        "Programming",
        "Desain Aplikasi",
        "Analisis Data & Bisnis",
        "Jaringan & Keamanan",
        "Teknologi Umum"
    ])

    bakat = st.selectbox("🧠 Bakat utama kamu:", [
        "Logika & Algoritma",
        "Kreativitas",
        "Komunikasi & Analisis",
        "Teknis & Hardware",
        "Problem Solving"
    ])

    kepribadian = st.selectbox("👤 Gaya kamu:", [
        "Suka kerja sendiri (deep focus)",
        "Suka kerja tim",
        "Suka eksplor & belajar hal baru",
        "Suka hal teknis & detail"
    ])

    if st.button("🎯 Analisis Sekarang"):
        st.session_state['hasil'] = (minat, bakat, kepribadian)

# OUTPUT
with col2:
    st.subheader("📊 Hasil Analisis")

    if 'hasil' in st.session_state:
        m, b, k = st.session_state['hasil']

        skor = 0

        # TEKNIK INFORMATIKA
        if m == "Programming" and b in ["Logika & Algoritma", "Problem Solving"]:
            skor = 90
            prodi = "Teknik Informatika"
            deskripsi = """
Kamu punya pola pikir logis dan ketertarikan kuat di dunia coding 🔥  
Ini kombinasi ideal untuk menjadi problem solver di dunia teknologi.

🎯 Kamu akan belajar:
- Algoritma & struktur data
- Artificial Intelligence & Machine Learning
- Backend & sistem kompleks

🚀 Karier potensial:
Software Engineer, AI Engineer, Backend Developer
"""

        # SISTEM INFORMASI
        elif m == "Analisis Data & Bisnis" and b == "Komunikasi & Analisis":
            skor = 85
            prodi = "Sistem Informasi"
            deskripsi = """
Kamu punya kemampuan memahami kebutuhan bisnis sekaligus teknologi 📊  

🎯 Kamu akan belajar:
- Analisis sistem informasi
- Manajemen proyek IT
- Business Intelligence

🚀 Karier potensial:
Business Analyst, IT Consultant, System Analyst
"""

        # RPL
        elif m == "Desain Aplikasi" and b in ["Kreativitas", "Problem Solving"]:
            skor = 88
            prodi = "Rekayasa Perangkat Lunak"
            deskripsi = """
Kamu kreatif dan suka membangun sesuatu dari ide menjadi produk nyata 🎨💻  

🎯 Kamu akan belajar:
- UI/UX Design
- Software Engineering
- Mobile & Web Development

🚀 Karier potensial:
Frontend Developer, App Developer, UI/UX Engineer
"""

        # TEKNOLOGI INFORMASI
        elif m == "Jaringan & Keamanan" and b == "Teknis & Hardware":
            skor = 87
            prodi = "Teknologi Informasi"
            deskripsi = """
Kamu suka dunia teknis dan infrastruktur digital 🌐  

🎯 Kamu akan belajar:
- Networking & server
- Cyber Security
- Cloud & DevOps

🚀 Karier potensial:
Network Engineer, Cyber Security Analyst, DevOps Engineer
"""

        else:
            skor = 70
            prodi = "Eksplorasi Dulu"
            deskripsi = """
Minat dan bakatmu masih fleksibel 🌟  

🎯 Saran:
- Coba belajar coding dasar
- Eksplor UI/UX
- Coba data analysis

Setelah eksplorasi, kamu akan lebih yakin memilih prodi yang tepat.
"""

        # OUTPUT UI
        st.success(f"🎯 Rekomendasi Kamu: {prodi}")

        st.markdown("### 🔥 Tingkat Kecocokan")
        st.progress(skor / 100)
        st.write(f"**Skor Kecocokan: {skor}%**")

        st.markdown("### 📖 Insight Untuk Kamu")
        st.info(deskripsi)

        # Insight tambahan
        with st.expander("📌 Tips Pengembangan Diri"):
            st.write("""
- Ikuti course online (Dicoding, Coursera)
- Bangun project kecil (portfolio)
- Ikut komunitas IT
- Konsisten belajar 1% setiap hari
""")

        with st.expander("⚠️ Hal yang Perlu Diperhatikan"):
            st.write("""
- Jangan ikut-ikutan teman
- Kenali gaya belajarmu
- Fokus ke skill, bukan hanya gelar
""")

# TABEL
st.divider()
st.markdown("## 📋 Perbandingan Prodi Informatika")

data = {
    "Prodi": [
        "Teknik Informatika",
        "Sistem Informasi",
        "Rekayasa Perangkat Lunak",
        "Teknologi Informasi"
    ],
    "Fokus": [
        "Algoritma & Programming",
        "Bisnis & Sistem",
        "Pengembangan Aplikasi",
        "Jaringan & Infrastruktur"
    ],
    "Level Coding": [
        "Tinggi 🔥",
        "Sedang ⚖️",
        "Tinggi 🔥",
        "Rendah - Sedang"
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)