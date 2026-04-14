import streamlit as st

st.title("Audio & Video Player")
st.divider()

# Upload audio
audio_file = st.file_uploader(
    "Upload Audio",
    type=["mp3", "ogg"]
)

# Upload video
video_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "mkv"]
)

# Button
if st.button("Play ▶️"):
    # ❌ No file uploaded
    if audio_file is None and video_file is None:
        st.error("Please upload an audio or video file ❌") 
    # error age tekei show hoiee takee warnnig button clicker por
    
    else:
        # ▶️ Play audio
        if audio_file is not None:
            st.success("Playing audio 🎵")
            st.audio(audio_file)

        # ▶️ Play video
        if video_file is not None:
            st.success("Playing video 🎬")
            st.video(video_file)