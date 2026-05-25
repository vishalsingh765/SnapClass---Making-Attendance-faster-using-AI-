
import streamlit as st


# =========================
# HOME PAGE BACKGROUND
# =========================
def style_background_home():

    st.markdown("""
    <style>

    /* MAIN APP BACKGROUND */
    .stApp {
        background: #5865F2  !important;
    }

    /* STUDENT & TEACHER CARD */
    div[data-testid="column"] > div {
        background-color: #E0E3FF;
        padding: 2.5rem;
        border-radius: 30px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        text-align: center;
        transition: all 0.3s ease-in-out;
        height: 100%;
    }

    /* HOVER EFFECT */
    div[data-testid="column"] > div:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.25);
    }

    </style>
    """, unsafe_allow_html=True)


# =========================
# DASHBOARD BACKGROUND
# =========================
def style_background_dashboard():

    st.markdown("""
    <style>

    /* Main Background */
    .stApp {
       background:#7842f5 !important;
    }

    /* Global Text */
    html, body, [class*="css"]  {
        color: #111827 !important;
    }

    /* Input Fields */
    .stTextInput input {
        background-color: white !important;
        color: #111827 !important;
        -webkit-text-fill-color: #111827 !important;
        caret-color: #111827 !important;

        border-radius: 12px !important;
        border: 1px solid #CBD5E1 !important;

        padding: 10px !important;
        font-size: 15px !important;
    }

    /* Placeholder */
    .stTextInput input::placeholder {
        color: #64748B !important;
        opacity: 1 !important;
    }

    /* Labels */
    .stTextInput label {
        color: #111827 !important;
        font-weight: 700 !important;
    }

    /* Buttons */
    .stButton button {

        background: #5865F2 !important;
        color: white !important;

        border: none !important;
        border-radius: 12px !important;

        padding: 10px 18px !important;

        font-weight: 700 !important;

        transition: 0.2s ease-in-out !important;
    }

    .stButton button:hover {
        background: #4752C4 !important;
        transform: translateY(-1px);
    }

    /* Cards */
    div[data-testid="stVerticalBlock"] > div:has(div[style*="border-radius"]) {

        color: #111827 !important;
    }

    /* Markdown Text */
    .stMarkdown,
    .stMarkdown p,
    .stMarkdown span,
    .stMarkdown div {
        color: #111827 !important;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #111827 !important;
    }

    /* Success Message */
    .stSuccess {
        background-color: #DCFCE7 !important;
        color: #166534 !important;
    }

    /* Warning Message */
    .stWarning {
        background-color: #FEF3C7 !important;
        color: #92400E !important;
    }

    /* Error Message */
    .stError {
        background-color: #FEE2E2 !important;
        color: #991B1B !important;
    }

    </style>
    """, unsafe_allow_html=True)


# =========================
# GLOBAL BASE LAYOUT
# =========================
def style_base_layout():

    st.markdown("""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

    /* HIDE STREAMLIT DEFAULT MENU */
    #MainMenu,
    footer,
    header {
        visibility: hidden;
    }

    /* PAGE SPACING */
    .block-container {
        padding-top: 1.5rem !important;
        padding-left: 4rem !important;
        padding-right: 4rem !important;
    }

    /* MAIN TITLE */
    h1 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 4rem !important;
        line-height: 1.1 !important;
        margin-bottom: 0rem !important;
        text-align: center;
        color: white !important;
    }

    /* SUB HEADINGS */
    h2 {
        font-family: 'Climate Crisis', sans-serif !important;
        font-size: 2rem !important;
        line-height: 1 !important;
        margin-bottom: 1rem !important;
        text-align: center;
        color: black !important;
    }

    /* NORMAL TEXT */
    h3,
    h4,
    h5,
    h6,
    p {
        font-family: 'Outfit', sans-serif !important;
    }

    /* BUTTONS */
    button {
        border-radius: 1.5rem !important;
        background-color: #5865F2 !important;
        color: white !important;
        padding: 10px 20px !important;
        border: none !important;
        transition: all 0.25s ease-in-out !important;
        font-weight: 600 !important;
    }

    /* SECONDARY BUTTON */
    button[kind="secondary"] {
        background-color: #EB459E !important;
    }

    /* TERTIARY BUTTON */
    button[kind="tertiary"] {
        background-color: black !important;
    }

    /* BUTTON HOVER */
    button:hover {
        transform: scale(1.05);
    }

    </style>
    """, unsafe_allow_html=True)