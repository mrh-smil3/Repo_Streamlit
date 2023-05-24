import streamlit as st

def main():
    # Judul
    st.title("Portofolio Saya")

    # Deskripsi
    st.write("""
    Selamat datang di portofolio saya! Saya adalah seorang pengembang perangkat lunak dengan minat utama dalam pembangunan web dan kecerdasan buatan.
    """)
    
    # Informasi Pribadi
    st.header("Informasi Pribadi")
    st.subheader("Nama")
    st.write("John Doe")
    st.subheader("Email")
    st.write("johndoe@example.com")
    st.subheader("Lokasi")
    st.write("Jakarta, Indonesia")

    # Pendidikan
    st.header("Pendidikan")
    st.subheader("Sarjana Teknik Informatika")
    st.write("Universitas ABC (2015-2019)")

    # Pengalaman Kerja
    st.header("Pengalaman Kerja")
    st.subheader("Pengembang Perangkat Lunak")
    st.write("Perusahaan XYZ (2019-2021)")
    st.write("- Mengembangkan aplikasi web menggunakan Python dan Flask.")
    st.write("- Memelihara basis data dan menerapkan perubahan sesuai kebutuhan.")

    # Proyek
    st.header("Proyek")
    st.subheader("Aplikasi Pencarian Gambar")
    st.write("- Mengembangkan aplikasi pencarian gambar menggunakan Python dan Django.")
    st.write("- Menggunakan API Pexels untuk mendapatkan gambar.")

    st.subheader("Sistem Rekomendasi Film")
    st.write("- Mengembangkan sistem rekomendasi film menggunakan Python dan Scikit-learn.")
    st.write("- Menggunakan dataset IMDb untuk membangun model rekomendasi.")

    # Footer
    st.write("---")
    st.write("Terima kasih telah mengunjungi portofolio saya.")

if __name__ == '__main__':
    main()
