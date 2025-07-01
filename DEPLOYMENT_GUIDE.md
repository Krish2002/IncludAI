# Deployment Guide for IncludAI Bot

This guide will help you deploy both your chatbot and website to the cloud so they're accessible to everyone.

## 🚀 Quick Start Options

### Option 1: Streamlit Cloud (Recommended for Chatbot)
**Cost**: Free tier available
**Difficulty**: Easy
**Best for**: Chatbot deployment

### Option 2: Railway/Render (Alternative for Chatbot)
**Cost**: Free tier available
**Difficulty**: Medium
**Best for**: Chatbot deployment

### Option 3: Netlify/Vercel (For Website)
**Cost**: Free tier available
**Difficulty**: Easy
**Best for**: Static website deployment

---

## 📋 Prerequisites

1. **GitHub Account**: You'll need to push your code to GitHub
2. **Google AI API Key**: Your existing API key
3. **Domain Name** (Optional): For a custom URL

---

## 🎯 Step-by-Step Deployment

### Step 1: Prepare Your Repository

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit for deployment"
   ```

2. **Create GitHub Repository**:
   - Go to [GitHub](https://github.com)
   - Create a new repository
   - Push your code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy Chatbot to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub

2. **Deploy Your App**:
   - Click "New app"
   - Select your repository
   - Set the path to: `chatbot/streamlit_app.py`
   - Click "Deploy"

3. **Configure Environment Variables**:
   - In your app settings, add:
     - Key: `GOOGLE_API_KEY`
     - Value: Your Google AI API key

4. **Your chatbot will be live at**: `https://your-app-name.streamlit.app`

### Step 3: Deploy Website to Netlify

1. **Go to Netlify**:
   - Visit [netlify.com](https://netlify.com)
   - Sign up with GitHub

2. **Deploy Site**:
   - Click "New site from Git"
   - Choose your repository
   - Set build command: (leave empty for static site)
   - Set publish directory: `.` (root directory)
   - Click "Deploy site"

3. **Your website will be live at**: `https://your-site-name.netlify.app`

### Step 4: Link Chatbot to Website

1. **Update Website Links**:
   - Edit your HTML files to link to your Streamlit chatbot URL
   - Add a "Try Our Chatbot" button that links to the Streamlit app

2. **Example Update** (in `index.html`):
   ```html
   <a href="https://your-app-name.streamlit.app" class="btn btn-primary">Try Our Chatbot</a>
   ```

---

## 🔧 Alternative Deployment Options

### Railway (Alternative to Streamlit Cloud)

1. **Go to Railway**:
   - Visit [railway.app](https://railway.app)
   - Sign in with GitHub

2. **Deploy**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Set environment variables
   - Deploy

### Render (Alternative to Streamlit Cloud)

1. **Go to Render**:
   - Visit [render.com](https://render.com)
   - Sign up with GitHub

2. **Deploy**:
   - Click "New Web Service"
   - Connect your repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `streamlit run chatbot/streamlit_app.py --server.port $PORT`
   - Add environment variables
   - Deploy

---

## 🔒 Security Considerations

1. **API Key Security**:
   - Never commit API keys to Git
   - Use environment variables in production
   - Consider using a secrets management service

2. **Environment Variables**:
   - Set `GOOGLE_API_KEY` in your cloud platform's environment variables
   - Keep your API key secure and rotate it regularly

---

## 📊 Monitoring & Maintenance

1. **Check Logs**:
   - Monitor your app's performance
   - Check for errors in the cloud platform's dashboard

2. **Update Dependencies**:
   - Regularly update your `requirements.txt`
   - Test locally before deploying updates

3. **Backup**:
   - Keep local backups of your code
   - Use Git for version control

---

## 🆘 Troubleshooting

### Common Issues:

1. **Import Errors**:
   - Ensure all dependencies are in `requirements.txt`
   - Check file paths are correct

2. **API Key Issues**:
   - Verify environment variables are set correctly
   - Check API key permissions

3. **Deployment Failures**:
   - Check build logs for errors
   - Ensure all files are committed to Git

### Getting Help:
- Check the platform's documentation
- Look at error logs in the deployment dashboard
- Test locally first

---

## 🎉 Success!

Once deployed, your chatbot and website will be:
- ✅ Accessible 24/7
- ✅ Available worldwide
- ✅ No need to run on your laptop
- ✅ Professional URLs
- ✅ Scalable and reliable

**Your URLs will be**:
- Website: `https://your-site-name.netlify.app`
- Chatbot: `https://your-app-name.streamlit.app`

---

## 📞 Next Steps

1. **Custom Domain** (Optional):
   - Purchase a domain name
   - Configure DNS settings
   - Set up custom URLs

2. **Analytics**:
   - Add Google Analytics to your website
   - Monitor chatbot usage

3. **Backup Strategy**:
   - Set up automated backups
   - Document your deployment process

4. **Scaling**:
   - Monitor usage and performance
   - Consider paid tiers if needed 