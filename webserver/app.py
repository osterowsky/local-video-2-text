import streamlit as st
from businessLogic import transcribeYoutubeVideo, transcribeLocalVideo, save_transcription, cleanup_old_files


def open_buy_me_coffee():
    st.markdown('<script>document.getElementById("buy-me-coffee-btn").click();</script>',
                unsafe_allow_html=True)

def error_handling_transcription(transcript):
    if transcript:
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Error occurred while transcribing.")
        st.write("Please try again.")

def main():
    url, localVideo = None, None

    st.title("Video2Text")
    # User input: YouTube URL
    ytOrLocal = st.radio("What you would like to transcribe?:", ("YouTube Video", "Local Video"))

    if ytOrLocal == "YouTube Video":
        url = st.text_input("Enter YouTube URL:")
    elif ytOrLocal == "Local Video":
        localVideo = st.file_uploader("Upload Local Video:")
        if localVideo:
            print(localVideo.name)

    # User input: model
    models = ["tiny", "base", "small", "medium", "large"]
    model = st.selectbox("Select Model:", models)
    st.write(
        "If you take a smaller model it is faster but not as accurate, whereas a larger model is slower but more accurate.")

    if 'transcript' not in st.session_state:
        st.session_state.transcript = ""
        st.session_state.word_file = None

    if st.button("Transcribe"):
        cleanup_old_files()
        if url:
            transcript = transcribeYoutubeVideo(url, model)
            error_handling_transcription(transcript)
        elif localVideo:
             transcript = transcribeLocalVideo(localVideo, model)
             error_handling_transcription(transcript)

        st.session_state.transcript = transcript
        st.session_state.word_file = save_transcription(transcript)

    # Initialize session state for transcript
    if st.session_state.transcript and st.session_state.word_file:
        with open(st.session_state.word_file, "rb") as file:
            st.download_button(label="Download Word Document",
                               data=file,
                               file_name=st.session_state.word_file,
                               mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


    st.markdown('<div style="margin-top: 450px;"</div>',
                unsafe_allow_html=True)

    st.write(
        "If you need help or have questions about Video2Text, feel free to reach out to me.")

    st.write("Please enter your message below:")
    user_message = st.text_area("Your Message:")

    st.markdown(
        f'<a href="mailto:contact@jhayer.tech?subject=Video2Text-Help&body={user_message}">Send Mail</a>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
