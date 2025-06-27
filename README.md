# 🤖 ElectroNova Assistant

A modern, interactive chatbot interface for ElectroNova, a consumer electronics company. This application provides a professional virtual assistant that can help customers with product information, order tracking, technical support, and more.

## ✨ Features

- **Modern Web Interface**: Beautiful, responsive design built with Streamlit
- **AI-Powered Responses**: Powered by Google's Gemini 2.5 Flash model
- **Chat History**: Persistent conversation history during the session
- **Quick Actions**: Pre-defined buttons for common queries
- **Professional Styling**: Clean, modern UI with custom CSS
- **Real-time Interaction**: Instant responses with loading indicators

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Generative AI API key

### Installation

1. **Clone or download this project**

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .\venv\Scripts\Activate.ps1
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Update the API key**:
   Open `chatbot_app.py` and replace the API key in line 67:
   ```python
   return genai.Client(api_key="YOUR_API_KEY_HERE")
   ```

6. **Run the application**:
   ```bash
   streamlit run chatbot_app.py
   ```

7. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## 🎯 Usage

### Main Features

1. **Chat Interface**: Type your questions in the text input at the bottom
2. **Quick Actions**: Use the sidebar buttons for common queries:
   - 📱 Product Info
   - 📦 Track Order
   - 🔧 Support
   - 💳 Warranty

3. **Chat Management**: 
   - Clear chat history using the sidebar button
   - View conversation history during the session

### Example Queries

- "Tell me about your latest smartphones"
- "I need to track my order #EN456789"
- "My laptop is running slow, what should I do?"
- "What's the warranty period for your products?"
- "Can you recommend a good gaming laptop?"

## 🛠️ Technical Details

### Architecture

- **Frontend**: Streamlit web framework
- **AI Backend**: Google Generative AI (Gemini 2.5 Flash)
- **Styling**: Custom CSS for modern appearance
- **State Management**: Streamlit session state

### Key Components

- `chatbot_app.py`: Main application file
- `requirements.txt`: Python dependencies
- `test.py`: Original test script (for reference)

### Customization

You can customize the chatbot by modifying:

1. **Prompt Template**: Edit the `CHATBOT_PROMPT` variable
2. **Styling**: Modify the CSS in the `st.markdown` section
3. **Quick Actions**: Add or modify buttons in the sidebar
4. **Company Information**: Update the company name and branding

## 🔧 Configuration

### Environment Variables

For production use, consider using environment variables for the API key:

```python
import os
api_key = os.getenv('GOOGLE_GENAI_API_KEY')
```

### Model Configuration

You can change the AI model by modifying the model parameter:

```python
response = client.models.generate_content(
    model="gemini-2.5-flash",  # Change this to other available models
    contents=final_prompt
)
```

## 📁 Project Structure

```
bot/
├── chatbot_app.py      # Main Streamlit application
├── test.py            # Original test script
├── requirements.txt   # Python dependencies
├── README.md         # This file
└── venv/             # Virtual environment (created during setup)
```

## 🤝 Contributing

Feel free to contribute to this project by:

1. Reporting bugs
2. Suggesting new features
3. Improving the UI/UX
4. Adding new capabilities

## 📄 License

This project is for educational and demonstration purposes.

## 🆘 Support

If you encounter any issues:

1. Check that all dependencies are installed correctly
2. Verify your API key is valid and has proper permissions
3. Ensure you're using Python 3.8 or higher
4. Check the Streamlit documentation for troubleshooting

---

**Happy chatting! 🤖✨** 