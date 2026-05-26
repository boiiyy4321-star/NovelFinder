import json
import streamlit as st

# No page config here; app.py handles it!
st.title("⭐ Top Recommendation")
st.write("The best, top-rated novels chosen just for you.")

try:
    with open("database_novels.json", "r", encoding="utf-8") as f:
        db = json.load(f)
except FileNotFoundError:
    db = {}

koleksi = db.get("koleksi_novel", {})
buku_populer = []

for genre, daftar_buku in koleksi.items():
    for buku in daftar_buku:
        if buku.get("rating", 0) >= 4.7:
            buku["genre"] = genre
            buku_populer.append(buku)

if not buku_populer:
    st.info("No top recommendations available with a rating of 4.7 or higher at the moment.")
else:
    for buku in buku_populer:
        with st.chat_message("assistant", avatar="🫧"):
            st.markdown(f"### **{buku.get('judul', 'Judul Buku')}**")
            
            # Using columns inside the subpage layout
            col1, col2 = st.columns([1, 2]) 
            
            with col1:
                if buku.get("image_url"):
                    st.image(buku.get("image_url"), use_container_width=True)
                else:
                    st.write("🖼️ *No Cover Available*")
                    
            with col2:
                st.write(f"✍️ **By:** {buku.get('penulis', '-')}")
                st.write(f"🏷️ **Genre:** {buku.get('genre', '-').title()}")
                st.write(f"📖 **Synopsis:** *{buku.get('sinopsis', '-')}*")
                st.success(f"🔥 Highly Recommended! Rating: {buku.get('rating', '-')}/5.0")
