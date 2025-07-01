#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
URL Updater Script for IncludAI Website
Usage: python update_urls.py [streamlit-url]
Example: python update_urls.py my-app.streamlit.app
"""

import sys
import re
import os

def update_urls(streamlit_url):
    """Update iframe URLs in HTML files"""
    if not streamlit_url.startswith('http'):
        streamlit_url = 'https://' + streamlit_url
    
    print(f"Updating URLs to: {streamlit_url}")
    
    html_files = ["services.html", "index.html"]
    
    for html_file in html_files:
        if os.path.exists(html_file):
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace localhost URLs
            updated_content = re.sub(
                r'src="http://localhost:8501"',
                f'src="{streamlit_url}"',
                content
            )
            
            updated_content = re.sub(
                r'http://localhost:8501',
                streamlit_url,
                updated_content
            )
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"✅ Updated {html_file}")
    
    print("\n🎉 URLs updated successfully!")
    print("\n📝 Next steps:")
    print("1. Commit and push changes: git add . && git commit -m 'Update chatbot URLs' && git push")
    print("2. Netlify will automatically redeploy")
    print("3. Test your integrated website")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python update_urls.py [streamlit-url]")
        print("Example: python update_urls.py my-app.streamlit.app")
        sys.exit(1)
    
    update_urls(sys.argv[1]) 