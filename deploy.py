#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deployment Helper Script for IncludAI Bot
This script helps prepare your project for cloud deployment.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def check_requirements():
    """Check if all required files exist"""
    print("Checking project requirements...")
    
    required_files = [
        "requirements.txt",
        "chatbot/main.py",
        "chatbot/streamlit_app.py",
        "chatbot/config.py",
        "index.html",
        "styles.css",
        "script.js"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("All required files found")
        return True

def check_git_status():
    """Check if the project is a git repository"""
    print("\nChecking Git status...")
    
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Git repository found")
            return True
        else:
            print("Not a Git repository")
            return False
    except FileNotFoundError:
        print("Git not installed")
        return False

def check_api_key():
    """Check if API key is configured"""
    print("\nChecking API key configuration...")
    
    config_file = "chatbot/config.py"
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
            if "GOOGLE_API_KEY" in content and "os.getenv" in content:
                print("API key configured to use environment variables")
                return True
            else:
                print("API key may be hardcoded - check config.py")
                return False
    else:
        print("Config file not found")
        return False

def create_deployment_checklist():
    """Create a deployment checklist"""
    print("\nCreating deployment checklist...")
    
    checklist = """# Deployment Checklist

## Pre-deployment Steps
- [ ] All files committed to Git
- [ ] API key configured as environment variable
- [ ] Requirements.txt updated
- [ ] Streamlit config created

## Deployment Steps

### For Chatbot (Streamlit Cloud):
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select your repository
5. Set path to: `chatbot/streamlit_app.py`
6. Add environment variable: GOOGLE_API_KEY = your_api_key
7. Click "Deploy"

### For Website (Netlify):
1. Go to https://netlify.com
2. Sign up with GitHub
3. Click "New site from Git"
4. Choose your repository
5. Set publish directory to: `.` (root)
6. Click "Deploy site"

## After Deployment:
- [ ] Update chatbot link in website
- [ ] Test both applications
- [ ] Share URLs with users

## Your URLs will be:
- Website: https://your-site-name.netlify.app
- Chatbot: https://your-app-name.streamlit.app
"""
    
    with open("DEPLOYMENT_CHECKLIST.md", "w", encoding='utf-8') as f:
        f.write(checklist)
    
    print("Deployment checklist created: DEPLOYMENT_CHECKLIST.md")

def main():
    """Main deployment helper function"""
    print("IncludAI Bot Deployment Helper")
    print("=" * 40)
    
    # Check requirements
    if not check_requirements():
        print("\nPlease fix missing files before deployment")
        return
    
    # Check Git status
    if not check_git_status():
        print("\nTo deploy, you'll need to:")
        print("1. Initialize Git: git init")
        print("2. Add files: git add .")
        print("3. Commit: git commit -m 'Initial commit'")
        print("4. Create GitHub repository and push")
    
    # Check API key
    check_api_key()
    
    # Create checklist
    create_deployment_checklist()
    
    print("\nDeployment preparation complete!")
    print("\nNext steps:")
    print("1. Read DEPLOYMENT_GUIDE.md for detailed instructions")
    print("2. Follow DEPLOYMENT_CHECKLIST.md")
    print("3. Deploy to Streamlit Cloud and Netlify")
    print("4. Update chatbot links in your website")

if __name__ == "__main__":
    main() 