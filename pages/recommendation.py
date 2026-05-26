import json
import streamlit as st

st.title("Top Recommendation")
st.write("The best, top-rated novels based on Goodreads ratings just for you.")

try:
    with open("database_novels.json", "r", encoding="utf-8") as f:
        db = json.load(f)
except FileNotFoundError:
    db = {}

koleksi = db.get("koleksi_novel", {})
buku_populer = []

for genre, daftar_buku in koleksi.items():
    for buku in daftar_buku:
        if buku.get("rating", 0) >= 4.0:
            buku["genre"] = genre
            buku_populer.append(buku)

if not buku_populer:
    st.info("No top recommendations available matching the criteria at this moment.")
else:
    for buku in buku_populer:
        with st.chat_message("assistant", avatar="🫧"):
            st.markdown(f"### **{buku.get('judul', 'Book Title')}**")
            
            col1, col2 = st.columns([1, 3]) # Gives clean poster layout scale
            
            with col1:
                if buku.get("image_url"):
                    st.image(buku.get("image_url"), use_container_width=True)
                else:
                    st.write("🖼️ *No Cover Available*")
                    
            with col2:
                st.write(f"**Author:** {buku.get('penulis', '-')}")
                st.write(f"**Genre:** {buku.get('genre', '-').title()}")
                st.write(f"**Synopsis:** *{buku.get('sinopsis', '-')}*")
                st.success(f"Goodreads Score: {buku.get('rating', '-')}/5.0")
