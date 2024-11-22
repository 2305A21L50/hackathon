
import streamlit as st

st.set_page_config(layout="wide", page_icon="image.png", page_title="Theorems")


LOGO_FULL = "logo2.jpeg"
LOGO_ICON = "image.png"

st.logo(LOGO_FULL, icon_image=LOGO_ICON, size="large")
st.image("logo.jpeg", use_container_width=True)


def another_page():
    st.write("Another page")


pages = {
    "Theorems": [
        st.Page("thevenins.py", title="Thevenin's theorem"),
        st.Page("nortons.py", title="Norton's theorem"),
    ],
    "Another page": [st.Page(another_page, title="Another page")],
}

pg = st.navigation(pages)
pg.run()
