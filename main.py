import time
import streamlit as st
from utils.eleven_labs import elevenlabs_voicer
from utils.myplayZ_ht import playht_voice
from utils.unreal_speach import unrealspeech_voice
from utils.youtube_transcript import get_youtube_transcript

# Function to play an audio file
audio_filename = 'audio.mp3'


def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')


selections = ['Unreal-Speech', 'Eleven Labs', 'Play HT']
# Sidebar for inputs
with st.sidebar:
    st.title("Insert a YouTube video link ")
    selected_model = st.selectbox(
        'Choose a TTS provider', selections)
    user_input = st.text_input("video url")

    if selected_model:
        st.session_state.select_value = selected_model

    if st.button('Submit'):
        with st.spinner('Fetching transcript...'):
            # Fetch and display the transcript
            transcript = get_youtube_transcript(user_input)
            st.session_state.transcript = transcript


# Display or clear chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"},
        {"role": "user", "content": "How may I assist you"}
    ]
# Display the transcript and generate audio
if 'transcript' in st.session_state:

    with st.chat_message('assistant'):
        st.write(st.session_state.transcript)

        start_time = time.time()  # Start time
        if st.session_state.select_value == selections[0]:
            with st.spinner('Audiobook generation is in progress...'):
                unrealspeech_voice(st.session_state.transcript)
        elif st.session_state.select_value == selections[1]:
            with st.spinner('Audiobook generation is in progress...'):
                elevenlabs_voicer(st.session_state.transcript)
        elif st.session_state.select_value == selections[2]:
            with st.spinner('Audiobook generation is in progress...'):
                playht_voice(st.session_state.transcript)
        end_time = time.time()  # End time
        time_taken = end_time - start_time  # Calculate time taken
        play_audio(audio_filename)
        st.session_state.transcript = time_taken
        if time_taken:
            st.button(
                f"Audio generation time: {time_taken:.2f} seconds")

st.chat_input('Ask me anything concerning video')
