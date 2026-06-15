import streamlit as st
import requests

st.title("YouTube Downloader")
url = st.text_input("Masukkan link YouTube:")

if st.button("Download Sekarang"):
    if url:
        try:
            st.write("Menghubungkan ke server...")
            
            # Format payload yang lebih standar untuk Cobalt API
            payload = {
                "url": url,
                "vCodec": "h264",
                "vQuality": "720"
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
            
            # Kita arahkan ke endpoint yang benar
            response = requests.post("https://api.cobalt.tools/api/json", json=payload, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                # Cobalt seringkali mengembalikan 'url' langsung
                if "url" in data:
                    st.success("Berhasil! Video siap.")
                    st.link_button("Klik untuk Simpan Video", data["url"])
                else:
                    st.error(f"API berhasil diakses, tapi tidak ditemukan link unduhan: {data}")
            else:
                # Menampilkan pesan error detail dari API
                st.error(f"API menolak permintaan (Status 400). Pastikan link benar. Detail: {response.text}")
                
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Masukkan link YouTube dulu!")
        
