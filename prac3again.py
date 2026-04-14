import streamlit as st
st.title("Audion and Video player")
st.divider()
#audio upload
Audio_upload=st.file_uploader("please upload audio",
                               type=["mp3", "ogg"])
#video upload
Video_upload=st.file_uploader("please upload video",
                              type=["MP4","MKV"])

if st.button("play all"):
    if Audio_upload is None and Video_upload is None:
        st.error("please upload audio and video")
    else:
        if Audio_upload is not None:
            st.success("Playing audio")
            st.audio(Audio_upload)    
        if Video_upload is not None:
            st.success("Playing video")
            st.video(Video_upload)        

          #st.video st.audio agola user
          # teke neya video play korte help kore  