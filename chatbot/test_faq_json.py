#!/usr/bin/env python3
"""
Test script to verify FAQ JSON functionality
"""

import json
import os

def test_faq_json():
    """Test the FAQ JSON file loading and acronym extraction"""
    
    # Test 1: Check if JSON file exists and is valid
    json_file_path = 'faq_data.json'
    if os.path.exists(json_file_path):
        print("✓ FAQ JSON file exists")
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                faqs = data.get('faqs', [])
                print(f"✓ JSON file loaded successfully with {len(faqs)} FAQs")
                
                # Test 2: Check structure of each FAQ
                for i, faq in enumerate(faqs, 1):
                    if 'question' in faq and 'answer' in faq and 'acronym' in faq:
                        print(f"✓ FAQ {i}: {faq['acronym']} - {faq['question'][:50]}...")
                    else:
                        print(f"✗ FAQ {i}: Missing required fields")
                        return False
                
                # Test 3: Extract acronyms
                acronyms = [faq.get('acronym', 'FAQ') for faq in faqs]
                print(f"✓ Extracted acronyms: {acronyms}")
                
                return True
                
        except json.JSONDecodeError as e:
            print(f"✗ JSON file is invalid: {e}")
            return False
        except Exception as e:
            print(f"✗ Error reading JSON file: {e}")
            return False
    else:
        print("✗ FAQ JSON file does not exist")
        return False

if __name__ == "__main__":
    print("Testing FAQ JSON functionality...")
    success = test_faq_json()
    if success:
        print("\n🎉 All tests passed! FAQ JSON system is working correctly.")
    else:
        print("\n❌ Some tests failed. Please check the FAQ JSON implementation.") 