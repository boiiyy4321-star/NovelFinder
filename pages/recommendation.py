import json
import streamlit as st

st.title("⭐ Top Recommendation")
st.write("Novel pilihan terbaik dengan rating tertinggi khusus buat kamu.")

# Membaca database novel lokal
try:
    with open("database_novels.json", "r", encoding="utf-8") as f:
        db = json.load(f)
except FileNotFoundError:
    db = {}

koleksi = db.get("koleksi_novel", {})
buku_populer = []

# Filter otomatis: Kumpulkan semua buku yang ratingnya >= 4.7
for genre, daftar_buku in koleksi.items():
    for buku in daftar_buku:
        if buku.get("rating", 0) >= 4.7:
            buku_populer.append(buku)

if not buku_populer:
    st.info("Belum ada rekomendasi teratas dengan rating ≥ 4.7 saat ini.")
else:
    # Tampilkan buku-buku terbaik
    for buku in buku_populer:
        with st.chat_message("assistant", avatar="📚"):
            st.markdown(f"### **{buku.get('judul', 'Judul Buku')}**")
            st.write(f"✍️ **Oleh:** {buku.get('penulis', '-')}")
            st.write(f"📖 **Sinopsis:** *{buku.get('sinopsis', '-')}*")
            st.success(f"🔥 Highly Recommended! Rating: {buku.get('rating', '-')}/5.0")