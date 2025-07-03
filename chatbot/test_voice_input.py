#!/usr/bin/env python3
"""
Test script to verify voice input functionality
"""

def test_voice_dependencies():
    """Test if all voice input dependencies are properly installed"""
    
    print("Testing voice input dependencies...")
    
    # Test 1: Check streamlit-mic-recorder
    try:
        from streamlit_mic_recorder import mic_recorder
        print("✓ streamlit-mic-recorder imported successfully")
    except ImportError as e:
        print(f"✗ streamlit-mic-recorder import failed: {e}")
        return False
    
    # Test 2: Check SpeechRecognition
    try:
        import speech_recognition as sr
        print("✓ SpeechRecognition imported successfully")
        
        # Test if recognizer can be initialized
        recognizer = sr.Recognizer()
        print("✓ Speech recognizer initialized successfully")
    except ImportError as e:
        print(f"✗ SpeechRecognition import failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Speech recognizer initialization failed: {e}")
        return False
    
    # Test 3: Check pyaudio
    try:
        import pyaudio
        print("✓ pyaudio imported successfully")
    except ImportError as e:
        print(f"✗ pyaudio import failed: {e}")
        return False
    
    # Test 4: Check tempfile (should be built-in)
    try:
        import tempfile
        print("✓ tempfile module available")
    except ImportError as e:
        print(f"✗ tempfile import failed: {e}")
        return False
    
    print("\n🎉 All voice input dependencies are properly installed!")
    print("\nVoice input features available:")
    print("- Microphone recording via streamlit-mic-recorder")
    print("- Speech-to-text transcription via Google Speech Recognition")
    print("- Audio processing via pyaudio")
    
    return True

if __name__ == "__main__":
    success = test_voice_dependencies()
    if not success:
        print("\n❌ Some dependencies are missing. Please install them using:")
        print("pip install streamlit-mic-recorder SpeechRecognition pyaudio") 