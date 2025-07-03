import streamlit as st
import sys
import os

# Add the chatbot directory to the path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import PAGE_CONFIG, COMPANY_NAME
from faq_handler import load_faq_data
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
    # Define or extract short FAQ topics (max 2 words)
    def extract_topic(question):
        # Use the first 2 significant words (skip numbers and stopwords)
        import re
        stopwords = {"what", "how", "can", "do", "is", "the", "a", "of", "on", "to", "for", "and", "in", "i", "you", "we", "your", "our", "with", "it", "are", "be", "an", "if", "or", "at", "by", "as", "from", "me", "my"}
        words = re.findall(r"\w+", question.lower())
        topic_words = [w.capitalize() for w in words if w not in stopwords and not w.isdigit()][:2]
        return " ".join(topic_words) if topic_words else question[:15]
    faq_topics = [extract_topic(item['question']) for item in faq_data]
    # Remove duplicates while preserving order
    seen = set()
    unique_faq_topics = []
    for t in faq_topics:
        if t and t not in seen:
            unique_faq_topics.append(t)
            seen.add(t)
    # Contextual suggestions: if user has asked something, show related topics
    if show_suggestions:
        suggestions = unique_faq_topics[:8]
        selected_question = render_faq_suggestions(suggestions)
        if selected_question:
            # Find the full FAQ question that matches the topic
            for item in faq_data:
                if extract_topic(item['question']) == selected_question:
                    selected_full_question = item['question']
                    break
            else:
                selected_full_question = selected_question
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
            # Find FAQ topics that share a word with the last user message
            related = []
            for idx, t in enumerate(unique_faq_topics):
                topic_words = set(t.lower().split())
                if any(word in last_user_message for word in topic_words):
                    related.append(t)
            # Fallback to general topics if none found
            suggestions = related[:4] if related else unique_faq_topics[:4]
            selected_question = render_faq_suggestions(suggestions)
            if selected_question:
                for item in faq_data:
                    if extract_topic(item['question']) == selected_question:
                        selected_full_question = item['question']
                        break
                else:
                    selected_full_question = selected_question
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