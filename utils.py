import base64
import streamlit as st
from config import LOGO_FILE_PATH

def get_image_as_base64(file_path):
    """Convert image to base64 for CSS background"""
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded_string}"
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

def format_conversation_history(conversation_history):
    """Format conversation history for AI prompt"""
    if conversation_history:
        formatted_history = ""
        for msg in conversation_history:
            if msg["role"] == "user":
                formatted_history += f"User: {msg['content']}\n"
            else:
                formatted_history += f"Assistant: {msg['content']}\n"
        return formatted_history
    else:
        return "No previous conversation."

def get_logo_base64():
    """Get logo as base64 string"""
    return get_image_as_base64(LOGO_FILE_PATH) 