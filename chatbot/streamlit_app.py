import streamlit as st
import sys
import os

# Add the chatbot directory to the path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import main

if __name__ == "__main__":
    main() 