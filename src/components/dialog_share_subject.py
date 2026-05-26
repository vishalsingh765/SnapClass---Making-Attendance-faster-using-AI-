import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):

    app_domain = "https://autoattendance.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    # ---------- CUSTOM CSS ----------
    st.markdown("""
    <style>

    /* Dialog main container */
    div[data-testid="stDialog"] {
        background-color: white !important;
        color: black !important;
    }

    /* Headers */
    div[data-testid="stDialog"] h1,
    div[data-testid="stDialog"] h2,
    div[data-testid="stDialog"] h3,
    div[data-testid="stDialog"] h4,
    div[data-testid="stDialog"] p,
    div[data-testid="stDialog"] label,
    div[data-testid="stDialog"] span {
        color: black !important;
    }

    /* Code blocks */
    div[data-testid="stDialog"] pre {
        background-color: #f5f5f5 !important;
        color: black !important;
        border-radius: 10px !important;
    }

    /* Info box */
    div[data-testid="stDialog"] .stAlert {
        background-color: #eef4ff !important;
        color: black !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- HEADER ----------
    st.header(f"{subject_name}")

    st.subheader("Scan to Join")

    # ---------- QR ----------
    qr = segno.make(join_url)

    out = io.BytesIO()

    qr.save(
        out,
        kind='png',
        scale=10,
        border=1
    )

    col1, col2 = st.columns(2)

    # ---------- LEFT ----------
    with col1:

        st.markdown("### Copy Link")

        st.code(join_url, language="text")

        st.markdown("### Subject Code")

        st.code(subject_code, language="text")

        st.info(
            "Copy this link and share it on WhatsApp, Email, or Classroom."
        )

    # ---------- RIGHT ----------
    with col2:

        st.markdown("### Scan to Join")

        st.image(
            out.getvalue(),
            caption="QR Code for Class Joining",
            use_container_width=True
        )
