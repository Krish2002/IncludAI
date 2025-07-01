import streamlit as st
import sys
import os

# Add the chatbot directory to the path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import PAGE_CONFIG
from ui_components import apply_custom_css, render_header, render_message, render_chat_input
from ai_service import get_bot_response

def main():
    """Main application function"""
    # Page configuration
    st.set_page_config(**PAGE_CONFIG)
    
    # Apply custom CSS
    apply_custom_css()
    
    # Render header
    render_header()
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize input counter for unique keys
    if "input_counter" not in st.session_state:
        st.session_state.input_counter = 0
    
    # Display messages
    for message in st.session_state.messages:
        render_message(message)
    
    # Render chat input
    user_input, submit_button = render_chat_input()
    
    # Handle form submission
    if submit_button and user_input.strip():
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get bot response
        with st.spinner(""):
            bot_response = get_bot_response(user_input, st.session_state.messages)
        
        # Add bot response to chat
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Increment input counter to force a new input field on next render
        st.session_state.input_counter += 1
        
        # Rerun to refresh the page
        st.rerun()
    
    # Clear chat button
    if st.button("Clear Chat", type="secondary"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main() 