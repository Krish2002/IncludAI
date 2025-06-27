import streamlit as st
from google import genai
import time
import re
import base64

# Load FAQ data
def load_faq_data():
    """Load FAQ data from the text file"""
    try:
        with open('electronics_company_faq.txt', 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Parse FAQ into questions and answers
        faq_data = []
        lines = content.split('\n')
        current_question = None
        current_answer = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if line starts with a number (FAQ question)
            if re.match(r'^\d+\.', line):
                # Save previous Q&A if exists
                if current_question and current_answer:
                    faq_data.append({
                        'question': current_question,
                        'answer': ' '.join(current_answer).strip()
                    })
                
                # Start new question
                current_question = line
                current_answer = []
            elif current_question and line:
                # This is part of the answer
                current_answer.append(line)
        
        # Add the last Q&A
        if current_question and current_answer:
            faq_data.append({
                'question': current_question,
                'answer': ' '.join(current_answer).strip()
            })
        
        return faq_data
    except Exception as e:
        st.error(f"Error loading FAQ file: {str(e)}")
        return []

def search_faq(user_question, faq_data):
    """Search FAQ for relevant answers"""
    if not faq_data:
        return None
    
    user_question_lower = user_question.lower()
    
    # Extract keywords from user question
    keywords = re.findall(r'\b\w+\b', user_question_lower)
    
    best_match = None
    best_score = 0
    
    for faq_item in faq_data:
        question_lower = faq_item['question'].lower()
        answer_lower = faq_item['answer'].lower()
        
        # Calculate match score based on keyword overlap
        score = 0
        for keyword in keywords:
            if len(keyword) > 2:  # Only consider words longer than 2 characters
                if keyword in question_lower:
                    score += 3  # Higher weight for question matches
                if keyword in answer_lower:
                    score += 1  # Lower weight for answer matches
        
        # Check for exact phrase matches
        if any(keyword in question_lower for keyword in ['warranty', 'return', 'refund', 'shipping', 'order', 'support', 'contact']):
            score += 2
        
        if score > best_score:
            best_score = score
            best_match = faq_item
    
    # Return match if score is above threshold
    if best_score >= 2:
        return best_match
    
    return None

def get_image_as_base64(file_path):
    """Convert image to base64 for CSS background"""
    try:
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return f"data:image/jpeg;base64,{encoded_string}"
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

# Load logo and convert to base64
logo_base64 = get_image_as_base64("logo_1.jpeg")

# Page configuration
st.set_page_config(
    page_title="Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Simple CSS for minimalistic design
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

# Initialize Google Generative AI
@st.cache_resource
def init_genai():
    return genai.Client(api_key="AIzaSyBoywC1-91_-s5md9HKkRQFxpK1j49tNQ0")

# Define the chatbot prompt
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
- Phone: +91 9876543210
- Email: support@pineapple.com
- Live Chat: Mon–Sat, 9 AM to 8 PM

Previous conversation:
{conversation_history}

FAQ content for current query: {faq_content}

Current user message: {user_message}

Please provide a helpful response based on the FAQ content if available, or direct to support if not found.
"""

def get_bot_response(user_message, conversation_history=None):
    """Get response from the AI model with conversation context and FAQ checking"""
    try:
        # First, check if the question is in our FAQ
        faq_data = load_faq_data()
        faq_match = search_faq(user_message, faq_data)
        
        # Format conversation history
        if conversation_history:
            formatted_history = ""
            for msg in conversation_history:
                if msg["role"] == "user":
                    formatted_history += f"User: {msg['content']}\n"
                else:
                    formatted_history += f"Assistant: {msg['content']}\n"
        else:
            formatted_history = "No previous conversation."
        
        if faq_match:
            # Use LLM to craft a response based on FAQ content
            client = init_genai()
            faq_content = f"Question: {faq_match['question']}\nAnswer: {faq_match['answer']}"
            
            final_prompt = CHATBOT_PROMPT.format(
                user_message=user_message,
                conversation_history=formatted_history,
                faq_content=faq_content
            )
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=final_prompt
            )
            
            return response.text
        else:
            # If no FAQ match, direct to customer support
            return """I couldn't find a specific answer to your question in our FAQ. 

For personalized assistance, please contact our customer support team:

📞 **Phone**: +91 9876543210
📧 **Email**: support@pineapple.com
💬 **Live Chat**: Available Mon–Sat, 9 AM to 8 PM

Our support team will be happy to help you with your specific inquiry and respond within 24 hours on business days."""
        
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again."

def main():
    # Header section with logo, company name, and description
    st.markdown("""
    <div class="header-section">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRsVMWDhnFq0mXRmLMUl9Cyts4OAB4Yy15VUg&s" 
             alt="PINEAPPLE Logo" 
             class="company-logo">
        <div class="company-name">PINEAPPLE</div>
        <div class="company-description">
            Leading manufacturer and distributor of innovative electronic products.<br>
            Empowering technology for a connected world.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Chat area
    # Display messages
    for message in st.session_state.messages:
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
    
    # Input area
    with st.form(key="user_input_form"):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            user_input = st.text_input(
                "",
                key="user_input",
                placeholder="Type your message...",
                label_visibility="collapsed"
            )
        
        with col2:
            submit_button = st.form_submit_button("Send", use_container_width=True)
    
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