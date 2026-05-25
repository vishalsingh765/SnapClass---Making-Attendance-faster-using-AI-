import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home

from src.ui.base_layout import (
    style_base_layout,
    style_background_home
)


def home_screen():

    header_home()

    style_background_home()

    style_base_layout()

    # =========================
    # CUSTOM BOX CSS
    # =========================
    st.markdown("""
    <style>

    div[data-testid="stColumn"] {
        background-color: white;
        padding: 30px;
        border-radius: 25px;
        text-align: center;

        box-shadow: 0px 4px 20px rgba(0,0,0,0.15);

        border: 2px solid #E0E3FF;

        transition: 0.3s;
    }

    div[data-testid="stColumn"]:hover {
        transform: translateY(-5px);
        box-shadow: 0px 8px 25px rgba(0,0,0,0.20);
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # TWO COLUMNS
    # =========================
    col1, col2 = st.columns(2, gap="large")

    # =========================
    # STUDENT BOX
    # =========================
    with col1:

        st.header("I'm Student")

        st.image(
            "https://i.ibb.co/844D9Lrt/mascot-student.png",
            width=120
        )

        st.write("Access attendance and classroom tools")

        if st.button(
            'Student Portal',
            type='primary',
            use_container_width=True
        ):

            st.session_state['login_type'] = 'student'

            st.rerun()

    # =========================
    # TEACHER BOX
    # =========================
    with col2:

        st.header("I'm Teacher")

        st.image(
            "https://i.ibb.co/CsmQQV6X/mascot-prof.png",
            width=145
        )

        st.write("Manage subjects and AI attendance")

        if st.button(
            'Teacher Portal',
            type='primary',
            use_container_width=True
        ):

            st.session_state['login_type'] = 'teacher'

            st.rerun()

    footer_home()