import json
import streamlit as st

st.set_page_config(
    page_title="NovelFinder", 
    page_icon="📚", 
    layout="wide"  # Keep wide layout for structured grid space
)

def home_page() -> None:
    # --- HERO SECTION ---
    st.title("Welcome to NovelFinder!")
    st.subheader("Your ultimate gateway to finding your next favorite book.")
    st.markdown(
        "Whether you know exactly what vibe you are looking for or want an AI assistant "
        "to guide your path, NovelFinder has you covered."
    )
    
    st.info("**Quick Start Guide:** Use the sidebar on the left to explore features!")
    st.divider()


    # --- FEATURED BOOK OF THE MONTH ---
    st.write("### Book of the Month Spotlight")
    
    featured_book = {
        "judul": "Project Hail Mary",
        "penulis": "Andy Weir",
        "rating": 4.51,
        "sinopsis": "A lone astronaut awakens in space with no memory of his mission, and he must use science to complete his quest to save Earth.",
        "image_url": "https://m.media-amazon.com/images/I/91ENQs2KLAL._AC_UF350,350_QL50_.jpg"
    }

    with st.container(border=True):
        col_img, col_txt = st.columns([1, 3]) # Balanced ratio for book image and description
        with col_img:
            st.image(featured_book["image_url"], use_container_width=True)
        with col_txt:
            st.markdown(f"## **{featured_book['judul']}**")
            st.markdown(f"**Author:** {featured_book['penulis']} | ⭐ **Goodreads:** {featured_book['rating']}/5.0")
            st.write(f"*{featured_book['sinopsis']}*")
            st.success("**Why it won this month:** An absolute masterpiece of hard science fiction. It keeps you on the edge of your seat from page one with unparalleled wit, pacing, and heart.")

    st.divider()

    # --- DISCOVER FEATURES SECTION ---
    st.write("### Discover The Features")
    col_rec, col_bot = st.columns(2)
    
    with col_rec:
        st.markdown("#### Top Recommendations")
        st.write(
            "Go straight to world's best novels with recommendations based on real Goodreads ratings."
            "Every book here carries an exceptionally high rating with detailed synopsis cards."
        )
        st.caption("👉 Click *Top Recommendation* in the sidebar to view.")

    with col_bot:
        st.markdown("#### FictionFinder AI Chatbot")
        st.write(
            "Have a highly specific storyline mood in mind? Talk directly with FictionFinder, "
            "an AI assistant designed to help you find your dream novel."
        )
        st.caption("👉 Click *FictionFinder* in the sidebar to chat.")

    st.divider()

    # --- TRENDING GENRES WITH IMAGES ---
    st.write("### 🏷️ Explore Popular Genres")
    g1, g2, g3, g4 = st.columns(4)
    
    with g1:
        st.image("https://www.thetolkienforum.com/wiki-asset/?pid=216&d=1627722014", use_container_width=True, caption="Fantasy")
    with g2:
        st.image("https://cdnpro.eraspace.com/media/mageplaza/blog/post/f/i/film_sci_fi_terbaik.jpg", use_container_width=True, caption="Sci-Fi")
    with g3:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQxMIMOgk4DGlncxNv4wGcmUDthtjeKcky-SA&s", use_container_width=True, caption="Romance")
    with g4:
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRlFZCXXrdmqDsQanRMTnY1HsdY8URFw_DpQ&s", use_container_width=True, caption="Thriller")


# --- SIDEBAR CONFIGURATION ---
st.sidebar.title("NovelFinder")
st.sidebar.write("Find Your Next Read!")

# --- NAVIGATION ROUTING ---
pages = [
    st.Page(home_page, title="Home", default=True),
    st.Page("pages/recommendation.py", title="Top Recommendation"),
    st.Page("pages/chatbot.py", title="FictionFinder")
]

pg = st.navigation(pages)
pg.run()
