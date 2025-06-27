import streamlit as st
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
        
        # Rerun to refresh the page
        st.rerun()
    
    # Clear chat button
    if st.button("Clear Chat", type="secondary"):
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main() 