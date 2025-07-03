import re
import streamlit as st
import sys
import os
import json

# Add the chatbot directory to the path so imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import FAQ_FILE_PATH

def load_faq_data():
    """Load FAQ data from the JSON file"""
    try:
        # Try to load from JSON file first
        json_file_path = os.path.join(os.path.dirname(FAQ_FILE_PATH), 'faq_data.json')
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get('faqs', [])
        
        # Fallback to text file if JSON doesn't exist
        with open(FAQ_FILE_PATH, 'r', encoding='utf-8') as file:
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
                        'answer': ' '.join(current_answer).strip(),
                        'acronym': 'FAQ'  # Default acronym for text file
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
                'answer': ' '.join(current_answer).strip(),
                'acronym': 'FAQ'  # Default acronym for text file
            })
        
        return faq_data
    except Exception as e:
        st.error(f"Error loading FAQ file: {str(e)}")
        return []

def get_faq_acronyms():
    """Get list of FAQ acronyms for suggestion box"""
    faq_data = load_faq_data()
    return [item.get('acronym', 'FAQ') for item in faq_data]

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