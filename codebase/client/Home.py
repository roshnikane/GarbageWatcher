import streamlit as st
from datetime import datetime

st.set_page_config(page_title="GarbageWatcher", page_icon="🗑️", layout="centered")

st.title("🗑️ GarbageWatcher")
st.write("Upload an image of a garbage bin/spot and submit for inspection.")

uploaded = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if uploaded is not None:
    st.image(uploaded, caption="Preview", use_container_width=True)

    submitted = st.button("Submit", type="primary")

    if submitted:
        st.success("Submitted successfully ✅")
        st.write("Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
else:
    st.info("Please upload an image to continue.")
