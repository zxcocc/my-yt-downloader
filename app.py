import streamlit as st

st.set_page_config(page_title="YT Downloader", page_icon="⬇️")

st.title("⬇️ YouTube Downloader")
st.write("Masukkan link video YouTube di bawah ini:")

url = st.text_input("Contoh: https://www.youtube.com/watch?v=...")

if st.button("Dapatkan Link Download"):
    if url and ("youtube.com" in url or "youtu.be" in url):
        # Mengambil ID Video
        video_id = url.split("v=")[-1] if "v=" in url else url.split("/")[-1]
        
        # Link ke layanan pengunduh pihak ketiga yang stabil
        download_url = f"https://snapsave.app/id/youtube/{video_id}"
        
        st.success("Tautan berhasil dibuat!")
        st.link_button("Klik di sini untuk Download", download_url)
        st.info("Anda akan diarahkan ke halaman unduhan eksternal yang stabil.")
    else:
        st.error("Masukkan link YouTube yang valid.")
        
