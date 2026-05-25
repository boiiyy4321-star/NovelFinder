import streamlit as st

st.set_page_config(page_title="NovelFinder", page_icon="📚")

def home_page() -> None:
    st.title("📚 Welcome to NovelFinder!")
    st.write("Find your favorite novels and get personalized recommendations!")
    st.info("Use the sidebar to navigate through the website")

st.sidebar.title("Navigation")

pages = [
    st.Page(home_page, title="Home", default=True),
    st.Page("pages/novel_list.py", title="Book Catalog"),
    st.Page("pages/recommendation.py", title="Top Recommendation"), # Fixed spelling to match file name
    st.Page("pages/chatbot.py", title="Novel Assistant")
]

pg = st.navigation(pages)
pg.run()
