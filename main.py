import time
import streamlit as st
from utils.eleven_labs import elevenlabs_voicer
from utils.myplayZ_ht import playht_voice
from utils.unreal_speach import unrealspeech_voice
from utils.youtube_transcript import get_youtube_transcript

audio_filename = 'audio.mp3'


def play_audio(file_path):
    with open(file_path, 'rb') as audio_file:
        st.audio(audio_file.read(), format='audio/mp3')


selections = ['Unreal-Speech', 'Eleven Labs', 'Play HT']

with st.sidebar:
    st.title("Insert a YouTube video link")
    user_input = st.text_input("video url")
    selected_model = st.selectbox('Choose a TTS provider', selections)

    if st.button('Submit'):
        if user_input and selected_model:
            try:
                with st.spinner('Fetching transcript...'):
                    transcript = get_youtube_transcript(user_input)
                    if transcript:
                        st.session_state.transcript = transcript
                        st.session_state.select_value = selected_model
            except Exception as e:
                st.error(f"Error fetching transcript: {e}")

if 'transcript' in st.session_state and 'select_value' in st.session_state:
    with st.chat_message('assistant'):
        st.write(st.session_state.transcript)

        try:
            start_time = time.time()
            if st.session_state.select_value == selections[0]:
                unrealspeech_voice(st.session_state.transcript)
            elif st.session_state.select_value == selections[1]:
                elevenlabs_voicer(st.session_state.transcript)
            elif st.session_state.select_value == selections[2]:
                playht_voice(st.session_state.transcript)
            play_audio(audio_filename)
            time_taken = time.time() - start_time
            st.info(f"Audio generation time: {time_taken:.2f} seconds")
        except Exception as e:
            st.error(f"Error during audio generation: {e}")

st.chat_input('Ask me anything concerning video')
