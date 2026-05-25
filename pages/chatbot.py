import os
import streamlit as st
import google.genai as genai

# REMOVED st.set_page_config to stop the multi-page crash
st.title("🤖 AI Book Recommendation Assistant")

# Load .env file from project root if present, so the app can use GEMINI_API_KEY there.
def load_env_file(env_path: str) -> None:
    if not os.path.exists(env_path):
        return
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and value and key not in os.environ:
                os.environ[key] = value

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
env_path = os.path.join(project_root, ".env")
load_env_file(env_path)

GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error(
        "Gemini API key not found. Please add `GEMINI_API_KEY` to `.streamlit/secrets.toml`, put it in `.env`, or set the environment variable `GEMINI_API_KEY`."
    )
    st.stop()

client = genai.Client(api_key=GEMINI_API_KEY)

# Contexting - Gemini can now suggest any real-world novel in a chill style
instruksi_sistem = """
Kamu adalah AI Kutu Buku yang ramah, asisten rekomendasi novel yang sangat ahli dan tahu banyak buku di dunia.
Tugasmu adalah membantu user memilih novel yang cocok untuk mereka baca.
Gunakan gaya bahasa yang santai, asyik, dan agak gaul (jaksel/anak muda) saat merespons agar seru.
Kamu BEBAS memberikan rekomendasi novel terkenal apa saja yang ada di dunia nyata berdasarkan preferensi, genre, atau mood yang diinginkan user.
Berikan informasi menarik seperti judul, penulis, dan alasan kenapa novel itu layak dibaca.
"""

# ==========================================
# MEMORI CHAT (SESSION STATE)
# ==========================================
if "riwayat_chat" not in st.session_state:
    st.session_state.riwayat_chat = [
        {"role": "assistant", "teks": "Hai gng, Looking for a fun novel to read? What genre are you looking for (Fantasy, Romance, or Mystery)?"}
    ]

# Tampilkan kembali semua pesan lama ke layar
for pesan in st.session_state.riwayat_chat:
    with st.chat_message(pesan["role"]):
        st.markdown(pesan["teks"])

# ==========================================
# KOTAK INPUT & LOGIKA BALASAN
# ==========================================
pertanyaan = st.chat_input("What novel you wanna read today?")

if pertanyaan:
    # A. Tampilkan dan simpan pesan User
    with st.chat_message("user"):
        st.markdown(pertanyaan)
    st.session_state.riwayat_chat.append({"role": "user", "teks": pertanyaan})

    # B. Gabungkan instruksi dan riwayat lama agar AI "Ingat" obrolan
    konteks_obrolan = instruksi_sistem + "\n\nRiwayat Obrolan:\n"
    for msg in st.session_state.riwayat_chat:
        konteks_obrolan += f"{msg['role']}: {msg['teks']}\n"

    # C. Panggil AI Gemini untuk menjawab
    with st.chat_message("assistant"):
        with st.spinner("Finding the best novel for you..."):
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=konteks_obrolan
                )
                jawaban = response.text
            except Exception as e:
                jawaban = f"NO! There's an error in the system: {e}"
            
            st.markdown(jawaban)

    # D. Simpan pesan Bot ke dalam memori
    st.session_state.riwayat_chat.append({"role": "assistant", "teks": jawaban})