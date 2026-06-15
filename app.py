import streamlit as st
import yt_dlp

st.title("YouTube Downloader Sederhana")
url = st.text_input("Masukkan link YouTube:")

if st.button("Download"):
    if url:
        ydl_opts = {'format': 'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            st.write("Sedang memproses...")
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            st.success(f"Berhasil! File siap: {filename}")
            
            # Menampilkan tombol download untuk user
            with open(filename, "rb") as file:
                st.download_button("Klik di sini untuk simpan ke HP", file, file_name=filename)
    else:
        st.warning("Masukkan link dulu!")
