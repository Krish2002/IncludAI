# Complete Website Deployment Guide

This guide will help you deploy your **complete website with integrated chatbot** to the cloud.

## 🎯 What We're Deploying

1. **Static Website** (HTML, CSS, JS) → Netlify
2. **Chatbot** (Streamlit App) → Streamlit Cloud  
3. **Integration** → Chatbot embedded in website

## 🚀 Step-by-Step Deployment

### Step 1: Deploy Chatbot to Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub

2. **Deploy Your App:**
   - Click "New app"
   - Repository: `Krish2002/IncludAI`
   - Branch: `main`
   - Main file path: `chatbot/streamlit_app.py`
   - Click "Deploy"

3. **Configure Environment Variables:**
   - In your app settings, add:
     - Key: `GOOGLE_API_KEY`
     - Value: Your Google AI API key

4. **Note Your Streamlit URL:**
   - It will be: `https://[your-app-name].streamlit.app`
   - Save this URL for the next step

### Step 2: Deploy Website to Netlify

1. **Go to Netlify:**
   - Visit [netlify.com](https://netlify.com)
   - Sign up/Login with GitHub

2. **Deploy Site:**
   - Click "New site from Git"
   - Choose GitHub repository: `Krish2002/IncludAI`
   - Branch: `main`
   - Build command: (leave empty)
   - Publish directory: `.` (root directory)
   - Click "Deploy site"

3. **Note Your Netlify URL:**
   - It will be: `https://[your-site-name].netlify.app`

### Step 3: Update Chatbot URLs

After both deployments are complete:

1. **Run the URL updater script:**
   ```bash
   python update_urls.py [your-streamlit-url]
   ```
   
   Example:
   ```bash
   python update_urls.py my-app.streamlit.app
   ```

2. **Commit and push changes:**
   ```bash
   git add .
   git commit -m "Update chatbot URLs for deployment"
   git push origin main
   ```

3. **Netlify will automatically redeploy** with the updated URLs

### Step 4: Test Everything

1. **Visit your Netlify website**
2. **Navigate to Services page**
3. **Test the embedded chatbot**
4. **Verify all links work correctly**

## 🎉 Final Result

You'll have:
- **Website**: `https://[your-site-name].netlify.app`
- **Chatbot**: `https://[your-app-name].streamlit.app`
- **Integrated**: Chatbot embedded directly in your website

## 🔧 Troubleshooting

### If chatbot doesn't load in iframe:
- Check if Streamlit app is running
- Verify environment variables are set
- Check browser console for CORS errors
- Try accessing the Streamlit URL directly

### If website doesn't deploy:
- Ensure all files are committed to Git
- Check Netlify build logs
- Verify `netlify.toml` configuration

### If iframe shows localhost:
- Run the `update_urls.py` script with correct Streamlit URL
- Commit and push changes
- Wait for Netlify to redeploy

## 📞 Support

If you encounter issues:
1. Check the deployment logs in both platforms
2. Verify all environment variables are set
3. Test each component individually
4. Check browser console for errors

## 🎯 Success Checklist

- [ ] Streamlit chatbot deployed and accessible
- [ ] Netlify website deployed and accessible  
- [ ] Chatbot URLs updated in HTML files
- [ ] Chatbot loads correctly in website iframe
- [ ] All website links and navigation work
- [ ] Mobile responsiveness maintained
- [ ] Contact forms and interactions work

---

**Congratulations!** Your complete website with integrated chatbot is now live and accessible to everyone worldwide! 🌍 