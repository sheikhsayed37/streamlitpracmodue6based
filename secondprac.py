import streamlit as st

st.title("Upload your image")

images = st.file_uploader(
    "Upload up to 3 images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if images:
    if len(images) > 3:
        st.error("Maximum 3 images allowed")
    
    else:
        if len(images) == 3:
            st.success("Exactly 3 images uploaded")

        cols = st.columns(len(images))  # col image e ai part toko same

        for i, img in enumerate(images):
            with cols[i]:
                st.image(img)