import streamlit as st
import sys
import os

# Add the chatbot directory to the path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import PAGE_CONFIG, COMPANY_NAME
from faq_handler import load_faq_data, get_faq_acronyms
from ui_components import apply_custom_css, render_header, render_message, render_chat_input, render_faq_suggestions
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
    
    # Add a default welcome message if the chat is empty
    if not st.session_state.messages:
        DEFAULT_WELCOME = (
            "Hello! I am the virtual assistant for {company}. "
            "Here are some topics I can help you with:"
        ).format(company=COMPANY_NAME)
        st.session_state.messages.append({"role": "assistant", "content": DEFAULT_WELCOME})
    
    # Initialize input counter for unique keys
    if "input_counter" not in st.session_state:
        st.session_state.input_counter = 0
    
    # Display messages
    for message in st.session_state.messages:
        render_message(message)
    
    # Only show FAQ suggestions if only the welcome message is present
    show_suggestions = (
        len(st.session_state.messages) == 1 and
        st.session_state.messages[0]["role"] == "assistant"
    )
    prefill = ""
    faq_data = load_faq_data()
    
    # Get FAQ acronyms for suggestion box
    faq_acronyms = get_faq_acronyms()
    
    # Contextual suggestions: if user has asked something, show related topics
    if show_suggestions:
        suggestions = faq_acronyms[:8]
        selected_acronym = render_faq_suggestions(suggestions)
        if selected_acronym:
            # Find the full FAQ question that matches the acronym
            for item in faq_data:
                if item.get('acronym') == selected_acronym:
                    selected_full_question = item['question']
                    break
            else:
                selected_full_question = selected_acronym
            st.session_state.messages.append({"role": "user", "content": selected_full_question})
            with st.spinner(""):
                bot_response = get_bot_response(selected_full_question, st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            st.session_state.input_counter += 1
            st.rerun()
    else:
        # After user message, show suggestions related to last user message
        last_user_message = None
        for m in reversed(st.session_state.messages):
            if m["role"] == "user":
                last_user_message = m["content"].lower()
                break
        if last_user_message:
            # Find FAQ acronyms that might be related to the last user message
            related = []
            for item in faq_data:
                acronym = item.get('acronym', '').lower()
                question_lower = item['question'].lower()
                answer_lower = item['answer'].lower()
                
                # Check if any word from the user message appears in the FAQ
                user_words = set(last_user_message.split())
                if any(word in question_lower or word in answer_lower for word in user_words if len(word) > 2):
                    related.append(item.get('acronym', 'FAQ'))
            
            # Fallback to general acronyms if none found
            suggestions = related[:4] if related else faq_acronyms[:4]
            selected_acronym = render_faq_suggestions(suggestions)
            if selected_acronym:
                for item in faq_data:
                    if item.get('acronym') == selected_acronym:
                        selected_full_question = item['question']
                        break
                else:
                    selected_full_question = selected_acronym
                st.session_state.messages.append({"role": "user", "content": selected_full_question})
                with st.spinner(""):
                    bot_response = get_bot_response(selected_full_question, st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
                st.session_state.input_counter += 1
                st.rerun()
        prefill = st.session_state.pop("prefill_input", "") if "prefill_input" in st.session_state else ""
    
    # Render chat input
    user_input, submit_button = render_chat_input(prefill)
    
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