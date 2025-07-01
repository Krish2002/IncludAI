import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Google AI API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyBoywC1-91_-s5md9HKkRQFxpK1j49tNQ0")
AI_MODEL = "gemini-2.5-flash"

# Company Information
COMPANY_NAME = "PINEAPPLE"
COMPANY_DESCRIPTION = "Leading manufacturer and distributor of innovative electronic products.\nEmpowering technology for a connected world."
COMPANY_LOGO_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsVMWDhnFq0mXRmLMUl9Cyts4OAB4Yy15VUg&s"

# Contact Information
CONTACT_INFO = {
    "phone": "+91 9876543210",
    "email": "support@pineapple.com",
    "live_chat": "Mon–Sat, 9 AM to 8 PM"
}

# File Paths
# Get the directory where this config file is located
CHATBOT_DIR = os.path.dirname(os.path.abspath(__file__))
FAQ_FILE_PATH = os.path.join(CHATBOT_DIR, "electronics_company_faq.txt")
LOGO_FILE_PATH = "logo_1.jpeg"

# Page Configuration
PAGE_CONFIG = {
    "page_title": "Chatbot",
    "page_icon": "💬",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

# Chatbot Prompt Template
CHATBOT_PROMPT = """
You are a helpful and professional virtual assistant for PINEAPPLE, a company that manufacture and sell electronic products.
Your role is to assist customers by providing well-crafted, concise responses inspired by our FAQ content.

When responding:
1. Keep responses short, clear, and to the point
2. Use a friendly and professional tone
3. If FAQ content is available, craft a natural response based on it
4. If no FAQ match is found, direct to customer support
5. Maintain conversation context when appropriate

Contact information for support:
- Phone: {phone}
- Email: {email}
- Live Chat: {live_chat}

Previous conversation:
{conversation_history}

FAQ content for current query: {faq_content}

Current user message: {user_message}

Please provide a helpful response based on the FAQ content if available, or direct to support if not found.
"""

# Default support response when no FAQ match is found
DEFAULT_SUPPORT_RESPONSE = """I couldn't find a specific answer to your question in our FAQ. 

For personalized assistance, please contact our customer support team:

📞 **Phone**: {phone}
📧 **Email**: {email}
💬 **Live Chat**: Available {live_chat}

Our support team will be happy to help you with your specific inquiry and respond within 24 hours on business days.""" 