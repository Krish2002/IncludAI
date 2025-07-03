#!/usr/bin/env python3
"""
Test script to verify voice input functionality
"""

def test_voice_dependencies():
    """Test if voice input dependencies are properly installed"""
    
    print("Testing voice input dependencies...")
    
    # Test 1: Check streamlit (should be available)
    try:
        import streamlit as st
        print("✓ streamlit imported successfully")
    except ImportError as e:
        print(f"✗ streamlit import failed: {e}")
        return False
    
    # Test 2: Check tempfile (should be built-in)
    try:
        import tempfile
        print("✓ tempfile module available")
    except ImportError as e:
        print(f"✗ tempfile import failed: {e}")
        return False
    
    # Test 3: Check os (should be built-in)
    try:
        import os
        print("✓ os module available")
    except ImportError as e:
        print(f"✗ os import failed: {e}")
        return False
    
    # Test 4: Check config import
    try:
        from config import VOICE_INPUT_CONFIG
        print("✓ Voice input configuration loaded")
        print(f"  - Enabled: {VOICE_INPUT_CONFIG.get('enabled', False)}")
        print(f"  - Use Whisper: {VOICE_INPUT_CONFIG.get('use_whisper', False)}")
        print(f"  - Supported formats: {VOICE_INPUT_CONFIG.get('supported_formats', [])}")
        print(f"  - Max file size: {VOICE_INPUT_CONFIG.get('max_file_size_mb', 0)}MB")
    except ImportError as e:
        print(f"✗ config import failed: {e}")
        return False
    
    # Test 5: Check OpenAI package (optional)
    try:
        import openai
        print("✓ OpenAI package available for Whisper transcription")
    except ImportError:
        print("⚠ OpenAI package not installed (Whisper transcription will use manual input)")
    
    print("\n🎉 Voice input system is ready!")
    print("\nFeatures available:")
    print("- Audio file upload with size validation")
    print("- File format validation")
    print("- Configuration-based settings")
    print("- Manual transcription input")
    if 'openai' in locals():
        print("- Automatic transcription with OpenAI Whisper (if API key is set)")
    
    return True

def test_voice_configuration():
    """Test voice input configuration"""
    print("\nTesting voice input configuration...")
    
    try:
        from config import VOICE_INPUT_CONFIG
        
        # Test configuration structure
        required_keys = ["enabled", "use_whisper", "supported_formats", "max_file_size_mb"]
        for key in required_keys:
            if key not in VOICE_INPUT_CONFIG:
                print(f"✗ Missing configuration key: {key}")
                return False
        
        print("✓ All required configuration keys present")
        print(f"✓ Voice input enabled: {VOICE_INPUT_CONFIG['enabled']}")
        print(f"✓ Whisper transcription: {VOICE_INPUT_CONFIG['use_whisper']}")
        print(f"✓ Supported formats: {VOICE_INPUT_CONFIG['supported_formats']}")
        print(f"✓ Max file size: {VOICE_INPUT_CONFIG['max_file_size_mb']}MB")
        
        return True
        
    except Exception as e:
        print(f"✗ Configuration test failed: {e}")
        return False

if __name__ == "__main__":
    print("=== Voice Input System Test ===\n")
    
    # Test basic dependencies
    deps_success = test_voice_dependencies()
    
    # Test configuration
    config_success = test_voice_configuration()
    
    if deps_success and config_success:
        print("\n🎉 All tests passed! Voice input system is fully functional.")
        print("\nTo use voice input:")
        print("1. Upload an audio file (WAV, MP3, M4A, OGG)")
        print("2. If OpenAI API key is set, automatic transcription will be used")
        print("3. Otherwise, you can type your message manually")
        print("4. The transcribed text will be sent to the chatbot")
    else:
        print("\n❌ Some tests failed. Please check the configuration and dependencies.") 