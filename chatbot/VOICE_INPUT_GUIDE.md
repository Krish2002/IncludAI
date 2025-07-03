# Voice Input Feature Guide

## Overview

The chatbot now includes a voice input feature that allows users to upload audio files and have them transcribed into text, which is then sent to the chatbot for processing.

## Features

### ✅ Available Features
- **Audio File Upload**: Support for WAV, MP3, M4A, and OGG formats
- **File Size Validation**: Maximum file size of 25MB (configurable)
- **Manual Transcription**: Fallback option to type messages manually
- **Configuration-Based**: Easy to enable/disable and customize
- **Error Handling**: Comprehensive error messages and status updates

### 🔄 Automatic Transcription (Optional)
- **OpenAI Whisper**: Automatic speech-to-text using OpenAI's Whisper API
- **API Key Required**: Set `OPENAI_API_KEY` environment variable
- **Fallback**: Manual transcription if Whisper is unavailable

## Configuration

The voice input feature can be configured in `config.py`:

```python
VOICE_INPUT_CONFIG = {
    "enabled": True,  # Set to False to disable voice input
    "use_whisper": True,  # Set to False to disable automatic transcription
    "supported_formats": ["wav", "mp3", "m4a", "ogg"],
    "max_file_size_mb": 25
}
```

## How to Use

### 1. Basic Usage (Manual Transcription)
1. Open the chatbot application
2. Scroll down to the "🎤 Voice Input" section
3. Click "Choose an audio file" and select your audio file
4. If automatic transcription is not available, you'll see a text input field
5. Type what you said in the audio file
6. The message will be sent to the chatbot

### 2. Advanced Usage (Automatic Transcription)
1. Install OpenAI package: `pip install openai`
2. Set your OpenAI API key: `export OPENAI_API_KEY="your-api-key"`
3. Upload an audio file
4. The system will automatically transcribe the audio
5. Review the transcription and send to chatbot

## Setup Instructions

### Prerequisites
```bash
# Install required packages
pip install streamlit openai python-dotenv

# Set OpenAI API key (optional, for automatic transcription)
export OPENAI_API_KEY="your-openai-api-key"
```

### Running the Application
```bash
# Navigate to the chatbot directory
cd chatbot

# Run the Streamlit app
streamlit run streamlit_app.py
```

## File Requirements

### Supported Formats
- **WAV**: Uncompressed audio (recommended for best quality)
- **MP3**: Compressed audio (good balance of size and quality)
- **M4A**: Apple's audio format
- **OGG**: Open source audio format

### File Size Limits
- **Maximum**: 25MB (configurable in `config.py`)
- **Recommended**: Under 10MB for faster processing

## Troubleshooting

### Common Issues

1. **"File too large" Error**
   - Reduce the audio file size
   - Use audio compression
   - Increase `max_file_size_mb` in config

2. **"OpenAI API key not found"**
   - Set the `OPENAI_API_KEY` environment variable
   - Or use manual transcription instead

3. **"OpenAI package not installed"**
   - Install with: `pip install openai`
   - Or use manual transcription

4. **"Could not understand audio"**
   - Ensure clear audio quality
   - Reduce background noise
   - Use manual transcription as fallback

### Testing the System
```bash
# Run the simple test
python test_voice_simple.py

# Run the comprehensive test (requires Streamlit secrets)
python test_voice_input.py
```

## Technical Details

### Architecture
- **File Upload**: Streamlit's `st.file_uploader`
- **File Processing**: Temporary file storage with automatic cleanup
- **Transcription**: OpenAI Whisper API or manual input
- **Integration**: Seamless integration with existing chatbot flow

### Security
- Temporary files are automatically deleted
- No audio files are permanently stored
- API keys are handled securely via environment variables

### Performance
- File size validation prevents large uploads
- Asynchronous processing with status updates
- Graceful fallback to manual input

## Customization

### Adding New Audio Formats
Edit `config.py`:
```python
VOICE_INPUT_CONFIG = {
    "supported_formats": ["wav", "mp3", "m4a", "ogg", "flac", "aac"]
}
```

### Changing File Size Limits
```python
VOICE_INPUT_CONFIG = {
    "max_file_size_mb": 50  # Increase to 50MB
}
```

### Disabling Voice Input
```python
VOICE_INPUT_CONFIG = {
    "enabled": False  # Completely disable voice input
}
```

## Future Enhancements

Potential improvements for future versions:
- Real-time microphone recording
- Multiple language support
- Audio preprocessing for better transcription
- Integration with other speech recognition services
- Voice output (text-to-speech) for bot responses

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify your configuration settings
3. Test with the provided test scripts
4. Check the Streamlit logs for detailed error messages 