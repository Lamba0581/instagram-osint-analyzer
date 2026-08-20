import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Instagram OSINT Analyzer",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 Instagram Public-Profile OSINT Analyzer")
st.caption("Educational OSINT dashboard for publicly available information")

username = st.text_input("Instagram username", placeholder="example_user")

if st.button("Analyze", type="primary"):
    username = username.strip().lstrip("@")

    if not username:
        st.warning("Please enter a username.")
    else:
        profile_url = f"https://www.instagram.com/{username}/"

        st.subheader("Profile")
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Username:**", username)
            st.write("**Profile URL:**", profile_url)

        with col2:
            st.write(
                "**Collected:**",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )

        st.info(
            "This starter version records the public profile target only. "
            "Future modules can add permitted public-data analysis."
        )

st.divider()
st.markdown("### ⚠️ Ethical Use")
st.write(
    "Use this project only for education and authorized OSINT research. "
    "Do not bypass authentication, access private accounts, collect credentials, "
    "or defeat platform security controls."
)
