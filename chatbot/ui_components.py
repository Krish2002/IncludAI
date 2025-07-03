import streamlit as st
import sys
import os
import tempfile
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder

# Add the chatbot directory to the path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import COMPANY_NAME, COMPANY_DESCRIPTION, COMPANY_LOGO_URL
from utils import get_logo_base64

def apply_custom_css():
    """Apply custom CSS styling to the application"""
    logo_base64 = get_logo_base64()
    
    st.markdown(f"""
    <style>
        .main {{
            padding: 1rem;
            max-width: 800px;
            margin: 0 auto;
            background-image: url('{logo_base64}');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            opacity: 0.1;
            position: relative;
        }}
        
        .main::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url('{logo_base64}');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            opacity: 0.1;
            z-index: -1;
        }}
        
        .header-section {{
            text-align: center;
            margin-bottom: 2rem;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }}
        
        .company-logo {{
            width: 80px;
            height: 80px;
            margin: 0 auto 1rem auto;
            border-radius: 50%;
            object-fit: cover;
        }}
        
        .company-name {{
            font-size: 2rem;
            font-weight: bold;
            color: #333;
            margin: 0.5rem 0;
            letter-spacing: 2px;
        }}
        
        .company-description {{
            font-size: 1rem;
            color: #666;
            margin: 0.5rem 0;
            line-height: 1.5;
        }}
        
        .message {{
            margin-bottom: 1rem;
            padding: 0.5rem;
        }}
        
        .message.user {{
            text-align: right;
        }}
        
        .message.bot {{
            text-align: left;
        }}
        
        .message-content {{
            display: inline-block;
            padding: 0.5rem 1rem;
            border-radius: 18px;
            max-width: 70%;
            word-wrap: break-word;
        }}
        
        .message-content.user {{
            background: #007bff;
            color: white;
        }}
        
        .message-content.bot {{
            background: #f8f9fa;
            color: #333;
            border: 1px solid #e0e0e0;
        }}
        
        .input-container {{
            display: flex;
            gap: 0.5rem;
            align-items: center;
        }}
        
        .stTextInput > div > div > input {{
            border: 1px solid #e0e0e0;
            border-radius: 20px;
            padding: 0.5rem 1rem;
        }}
        
        .stButton > button {{
            border-radius: 20px;
            padding: 0.5rem 1rem;
        }}
        
        .voice-input-section {{
            margin: 1rem 0;
            padding: 1rem;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            border: 2px solid #007bff;
        }}
        
        .voice-status {{
            margin: 0.5rem 0;
            padding: 0.5rem;
            border-radius: 5px;
        }}
        
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)

def render_header():
    """Render the header section with company information"""
    st.markdown(f"""
    <div class="header-section">
        <img src="{COMPANY_LOGO_URL}" 
             alt="{COMPANY_NAME} Logo" 
             class="company-logo">
        <div class="company-name">{COMPANY_NAME}</div>
        <div class="company-description">
            {COMPANY_DESCRIPTION}
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_message(message):
    """Render a single message in the chat"""
    if message["role"] == "user":
        st.markdown(f"""
        <div class="message user">
            <div class="message-content user">{message["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message bot">
            <div class="message-content bot">{message["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

def render_faq_suggestions(faq_questions):
    """Render up to 8 FAQ suggestion buttons in a 4x2 grid using columns, pineapple yellow background."""
    st.markdown("""
    <style>
    .suggestion-btn, .stButton > button {
        background: #FFE066 !important;
        color: #333 !important;
        border: none;
        border-radius: 18px !important;
        padding: 0.3rem 1.5rem !important;
        font-size: 0.95rem !important;
        min-width: 120px;
        cursor: pointer;
        transition: background 0.2s;
        box-shadow: 0 1px 4px rgba(0,0,0,0.07);
        display: inline-block;
        white-space: nowrap;
        margin-bottom: 0.5rem;
    }
    .suggestion-btn:hover, .stButton > button:hover {
        background: #FFD23F !important;
        color: #222 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    faq_questions = faq_questions[:8]
    clicked = None
    # Render 4 buttons per row, up to 2 rows
    for row_start in range(0, len(faq_questions), 4):
        cols = st.columns(4)
        for i in range(4):
            idx = row_start + i
            if idx < len(faq_questions):
                with cols[i]:
                    if st.button(faq_questions[idx], key=f"faq_suggestion_{idx}"):
                        clicked = faq_questions[idx]
    if clicked:
        return clicked
    return None

def render_chat_input(prefill=""):
    """Render the chat input form"""
    with st.form(key="user_input_form"):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            # Use dynamic key based on counter to force new input field
            input_key = f"user_input_{st.session_state.get('input_counter', 0)}"
            user_input = st.text_input(
                "",
                key=input_key,
                value=prefill,
                placeholder="Type your message...",
                label_visibility="collapsed"
            )
        
        with col2:
            submit_button = st.form_submit_button("Send", use_container_width=True)
    
    return user_input, submit_button 

def render_voice_input():
    """Render voice input section with microphone recorder"""
    st.markdown("""
    <div class="voice-input-section">
        <h4>🎤 Voice Input</h4>
        <p>Click the microphone to record your message</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create microphone recorder
    audio = mic_recorder(
        key="mic_recorder",
        use_container_width=True,
        sample_rate=16000,
        chunk_length_s=5,
        text="Click to record",
        recording_color="#e74c3c",
        neutral_color="#6c757d",
        icon_name="microphone",
        icon_size="2x"
    )
    
    transcript = ""
    
    if audio:
        # Show processing status
        with st.status("Processing audio...", expanded=True) as status:
            st.write("Transcribing your voice...")
            
            try:
                # Save audio to temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
                    tmpfile.write(audio['bytes'])
                    tmpfile.flush()
                    
                    # Initialize speech recognizer
                    recognizer = sr.Recognizer()
                    
                    # Read the audio file
                    with sr.AudioFile(tmpfile.name) as source:
                        # Adjust for ambient noise
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        # Record the audio
                        audio_data = recognizer.record(source)
                        
                        # Transcribe using Google Speech Recognition
                        transcript = recognizer.recognize_google(audio_data)
                        
                        status.update(label="✅ Transcription complete!", state="complete")
                        st.success(f"**Transcribed:** {transcript}")
                        
            except sr.UnknownValueError:
                status.update(label="❌ Could not understand audio", state="error")
                st.error("Sorry, I couldn't understand what you said. Please try again.")
            except sr.RequestError as e:
                status.update(label="❌ Transcription service error", state="error")
                st.error(f"Could not request results from speech recognition service; {e}")
            except Exception as e:
                status.update(label="❌ Error processing audio", state="error")
                st.error(f"An error occurred while processing the audio: {e}")
            finally:
                # Clean up temporary file
                if 'tmpfile' in locals():
                    try:
                        os.unlink(tmpfile.name)
                    except:
                        pass
    
    return transcript 