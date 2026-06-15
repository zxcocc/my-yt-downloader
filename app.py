import streamlit as st
import requests

st.title("YouTube Downloader (Fast & Stable)")
url = st.text_input("Masukkan link YouTube:")

if st.button("Download Sekarang"):
    if url:
        try:
            st.write("Sedang memproses permintaan Anda...")
            
            # Payload untuk API Cobalt
            payload = {
                "url": url,
                "vCodec": "h264",
                "vQuality": "720",
                "filenameStyle": "classic"
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            
            # Mengirim permintaan ke API
            response = requests.post("https://api.cobalt.tools/api/json", json=payload, headers=headers)
            data = response.json()
            
            # Memeriksa apakah respon berhasil
            if response.status_code == 200 and "url" in data:
                st.success("Berhasil! Video siap diunduh.")
                st.link_button("Klik untuk Simpan Video", data["url"])
            else:
                st.error("Gagal mendapatkan link. Pastikan link YouTube benar.")
        except Exception as e:
            st.error(f"Terjadi kesalahan teknis: {e}")
    else:
        st.warning("Masukkan link YouTube terlebih dahulu!")
