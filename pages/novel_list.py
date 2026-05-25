import json
import streamlit as st

st.title("📖 Book Catalog")
st.write("Jelajahi koleksi novel berdasarkan genre favoritmu.")

# Membaca database novel lokal
try:
    with open("database_novels.json", "r", encoding="utf-8") as f:
        db = json.load(f)
except FileNotFoundError:
    db = {}

koleksi = db.get("koleksi_novel", {})

if not koleksi:
    st.info("Katalog novel belum tersedia. Pastikan file database_novels.json sudah benar.")
else:
    # Loop melalui setiap genre (Fantasi, Romantis, Misteri)
    for genre, daftar_buku in koleksi.items():
        st.header(f"✨ Genre: {genre.capitalize()}")
        
        # Loop untuk menampilkan setiap buku di dalam genre tersebut
        for buku in daftar_buku:
            with st.container(border=True):
                st.subheader(buku.get("judul", "Judul Tidak Diketahui"))
                st.caption(f"✍️ Penulis: {buku.get('penulis', '-')} | ⭐ Rating: {buku.get('rating', '-')}/5.0")
                st.write(f"**Sinopsis:** {buku.get('sinopsis', 'Tidak ada sinopsis.')}")
                
                # Menampilkan tags/kategori kecil
                tags = buku.get("tags", [])
                if tags:
                    # Menggabungkan tags dengan format aesthetic
                    st.markdown(f"**Tags:** `{'` `'.join(tags)}`")