# Deployment Checklist

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
