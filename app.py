import streamlit as st
import yt_dlp

st.title("YouTube Downloader")
url = st.text_input("Masukkan link YouTube:")

if st.button("Download"):
    if url:
        try:
            st.write("Sedang memproses...")
            # Menambahkan 'noplaylist': True agar lebih stabil
            # Menggunakan format 'worstvideo+worstaudio/worst' agar server tidak perlu menggabungkan file berat
            ydl_opts = {
                'format': 'best', 
                'noplaylist': True,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
                # Menampilkan link download
                with open(filename, "rb") as file:
                    st.download_button("Klik untuk simpan ke HP", file, file_name=filename)
                st.success("Berhasil!")
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Catatan: Server mungkin sedang diblokir oleh YouTube. Coba lagi nanti atau gunakan video lain.")
    else:
        st.warning("Masukkan link dulu!")
        
