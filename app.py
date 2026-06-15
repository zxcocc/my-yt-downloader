import streamlit as st
import requests

st.title("YouTube Downloader (Stable API)")
url = st.text_input("Masukkan link YouTube:")

if st.button("Download Sekarang"):
    if url:
        try:
            st.write("Menghubungkan ke server pengunduh...")
            
            # Payload untuk API Cobalt
            # Kita menggunakan API publik cobalt.tools
            payload = {
                "url": url,
                "vCodec": "h264",
                "vQuality": "720"
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            
            response = requests.post("https://api.cobalt.tools/api/json", json=payload, headers=headers)
            data = response.json()
            
            # Jika respon dari API adalah 'redirect' atau 'url'
            if response.status_code == 200:
                if "url" in data:
                    st.success("Berhasil! Video siap.")
                    st.link_button("Klik untuk Simpan Video", data["url"])
                elif "status" in data and data["status"] == "redirect":
                    st.success("Video siap.")
                    st.link_button("Klik untuk Simpan Video", data["url"])
                else:
                    st.error(f"API merespon tapi tidak menemukan link: {data}")
            else:
                st.error(f"Gagal terhubung ke API. Status: {response.status_code}")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan teknis: {e}")
    else:
        st.warning("Masukkan link YouTube dulu!")
        
