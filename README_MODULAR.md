# PINEAPPLE Chatbot - Modular Structure

This chatbot application has been refactored into a modular structure for better maintainability and readability.

## File Structure

```
bot/
├── main.py                 # Main application entry point
├── config.py              # Configuration and constants
├── ai_service.py          # AI/LLM integration
├── faq_handler.py         # FAQ loading and searching
├── ui_components.py       # UI styling and components
├── utils.py               # Utility functions
├── __init__.py            # Package initialization
├── chatbot_app_backup.py  # Original monolithic file (backup)
└── README_MODULAR.md      # This file
```

## Module Descriptions

### `main.py`
- **Purpose**: Main application orchestrator
- **Responsibilities**: 
  - Initialize the Streamlit app
  - Coordinate between different modules
  - Handle user interactions and state management
  - Manage chat flow

### `config.py`
- **Purpose**: Centralized configuration management
- **Responsibilities**:
  - Store API keys and endpoints
  - Define company information
  - Configure page settings
  - Store prompt templates
  - Manage contact information

### `ai_service.py`
- **Purpose**: AI/LLM integration layer
- **Responsibilities**:
  - Initialize Google Generative AI client
  - Generate bot responses using FAQ data
  - Handle AI model interactions
  - Manage conversation context

### `faq_handler.py`
- **Purpose**: FAQ data management
- **Responsibilities**:
  - Load and parse FAQ data from text files
  - Search FAQ for relevant answers
  - Implement keyword matching algorithms
  - Score and rank FAQ matches

### `ui_components.py`
- **Purpose**: User interface components
- **Responsibilities**:
  - Apply custom CSS styling
  - Render header with company information
  - Display chat messages
  - Handle input forms and buttons

### `utils.py`
- **Purpose**: Utility functions
- **Responsibilities**:
  - Convert images to base64 for CSS
  - Format conversation history
  - Provide helper functions

## Benefits of Modular Structure

1. **Separation of Concerns**: Each module has a specific responsibility
2. **Maintainability**: Easier to update and debug individual components
3. **Reusability**: Components can be reused in other parts of the application
4. **Testability**: Individual modules can be tested in isolation
5. **Readability**: Code is more organized and easier to understand
6. **Scalability**: Easy to add new features or modify existing ones

## Running the Application

To run the modular chatbot application:

```bash
streamlit run main.py
```

## Migration from Monolithic Structure

The original `chatbot_app.py` has been preserved as `chatbot_app_backup.py`. The functionality remains exactly the same, but the code is now organized into logical modules.

## Adding New Features

When adding new features:

1. **Configuration**: Add constants to `config.py`
2. **Business Logic**: Create new modules or extend existing ones
3. **UI Components**: Add to `ui_components.py` or create new UI modules
4. **Utilities**: Add helper functions to `utils.py`
5. **Integration**: Update `main.py` to use new components

## Dependencies

The modular structure maintains the same dependencies as the original application:
- streamlit
- google-genai
- Other standard Python libraries 