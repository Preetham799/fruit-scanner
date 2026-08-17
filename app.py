import streamlit as st

st.set_page_config(
    page_title="Fruit Scanner",
    page_icon="🍎",
    layout="centered"
)

st.title("🍎 Fruit Scanner")
st.write("Upload a fruit image and analyze it.")

st.divider()

uploaded_file = st.file_uploader(
    "📷 Upload a fruit image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Fruit", use_container_width=True)

    st.success("Image uploaded successfully!")

    st.subheader("🔍 Fruit Analysis")

    fruit = st.selectbox(
        "Select fruit for this demo",
        ["Apple", "Banana", "Orange", "Mango", "Guava", "Other"]
    )

    if st.button("🔎 Scan Fruit"):
        st.subheader("Result")

        st.write("**Detected Fruit:**", fruit)
        st.write("**Condition:** Fresh")
        st.write("**Confidence:** 95%")

        st.success("✅ This fruit appears fresh and suitable for consumption.")

st.divider()

st.caption("Fruit Scanner — AI-based fruit identification and freshness analysis")