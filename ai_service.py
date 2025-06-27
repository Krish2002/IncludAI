import streamlit as st
from google import genai
from config import GOOGLE_API_KEY, AI_MODEL, CHATBOT_PROMPT, DEFAULT_SUPPORT_RESPONSE, CONTACT_INFO
from faq_handler import load_faq_data, search_faq
from utils import format_conversation_history

# Initialize Google Generative AI
@st.cache_resource
def init_genai():
    return genai.Client(api_key=GOOGLE_API_KEY)

def get_bot_response(user_message, conversation_history=None):
    """Get response from the AI model with conversation context and FAQ checking"""
    try:
        # First, check if the question is in our FAQ
        faq_data = load_faq_data()
        faq_match = search_faq(user_message, faq_data)
        
        # Format conversation history
        formatted_history = format_conversation_history(conversation_history)
        
        if faq_match:
            # Use LLM to craft a response based on FAQ content
            client = init_genai()
            faq_content = f"Question: {faq_match['question']}\nAnswer: {faq_match['answer']}"
            
            final_prompt = CHATBOT_PROMPT.format(
                user_message=user_message,
                conversation_history=formatted_history,
                faq_content=faq_content,
                phone=CONTACT_INFO["phone"],
                email=CONTACT_INFO["email"],
                live_chat=CONTACT_INFO["live_chat"]
            )
            
            response = client.models.generate_content(
                model=AI_MODEL,
                contents=final_prompt
            )
            
            return response.text
        else:
            # If no FAQ match, direct to customer support
            return DEFAULT_SUPPORT_RESPONSE.format(
                phone=CONTACT_INFO["phone"],
                email=CONTACT_INFO["email"],
                live_chat=CONTACT_INFO["live_chat"]
            )
        
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again." 