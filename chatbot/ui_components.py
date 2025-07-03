import streamlit as st
import sys
import os

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
    """Render up to 6 FAQ suggestion buttons in a horizontal row using columns, with soft pineapple yellow background (force override), and fix overlap. Keep 'Clear Chat' button white."""
    st.markdown("""
    <style>
    .suggestion-btn, .stButton > button[data-testid^="suggestion_"] {
        background: #FFE066 !important;
        color: #333 !important;
        border: none;
        border-radius: 18px !important;
        padding: 0.3rem 1.5rem !important;
        margin: 0.2rem 0.5rem 0.2rem 0 !important;
        font-size: 0.95rem !important;
        min-width: 120px;
        cursor: pointer;
        transition: background 0.2s;
        box-shadow: 0 1px 4px rgba(0,0,0,0.07);
        display: inline-block;
        white-space: nowrap;
    }
    .suggestion-btn:hover, .stButton > button[data-testid^="suggestion_"]:hover {
        background: #FFD23F !important;
        color: #222 !important;
    }
    /* Keep the Clear Chat button white */
    .stButton > button:has(span:contains('Clear Chat')) {
        background: #fff !important;
        color: #333 !important;
        border: 1px solid #e0e0e0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Only show up to 6 suggestions
    faq_questions = faq_questions[:6]
    cols = st.columns(len(faq_questions))
    clicked = None
    for idx, question in enumerate(faq_questions):
        with cols[idx]:
            if st.button(question, key=f"suggestion_{idx}"):
                clicked = question
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