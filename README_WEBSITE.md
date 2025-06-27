# PINEAPPLE Company Website

A modern, professional website for PINEAPPLE - an AI chatbot solutions company. The website features a responsive design with three main pages: Home, Services (with embedded chatbot), and Contact.

## 🚀 Features

- **Modern Design**: Clean, professional design with smooth animations
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Elements**: Hover effects, smooth scrolling, and form validation
- **Embedded Chatbot**: AI-powered chatbot integrated into the services page
- **Contact Form**: Functional contact form with validation
- **SEO Optimized**: Proper meta tags and semantic HTML structure

## 📁 File Structure

```
bot/
├── index.html              # Home page
├── services.html           # Services page with chatbot
├── contact.html            # Contact page
├── styles.css              # Main stylesheet
├── script.js               # JavaScript functionality
├── chatbot_app.py          # Streamlit chatbot application
├── logo.jpeg               # Company logo
├── electronics_company_faq.txt  # FAQ data for chatbot
├── requirements.txt        # Python dependencies
└── README_WEBSITE.md       # This file
```

## 🛠️ Setup Instructions

### 1. Start the Chatbot Server

First, you need to run the Streamlit chatbot application:

```bash
# Navigate to your project directory
cd /path/to/your/bot

# Activate virtual environment (if using one)
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies (if not already installed)
pip install -r requirements.txt

# Start the Streamlit chatbot server
streamlit run chatbot_app.py
```

The chatbot will be available at `http://localhost:8501`

### 2. Open the Website

Once the chatbot server is running, you can open the website:

1. **Using a Local Server** (Recommended):
   ```bash
   # Using Python's built-in server
   python -m http.server 8000
   
   # Or using Node.js (if you have it installed)
   npx serve .
   ```

2. **Direct File Opening**:
   - Simply double-click `index.html` to open it in your browser
   - Note: The chatbot iframe might not work with direct file opening due to CORS policies

### 3. Access the Website

- **Home Page**: `http://localhost:8000/index.html` or `http://localhost:8000/`
- **Services Page**: `http://localhost:8000/services.html`
- **Contact Page**: `http://localhost:8000/contact.html`

## 📱 Pages Overview

### Home Page (`index.html`)
- Hero section with company introduction
- About section with company description
- Services preview with key offerings
- Professional footer with contact information

### Services Page (`services.html`)
- Detailed service descriptions
- **Embedded chatbot** (requires Streamlit server running)
- Process overview
- Call-to-action section

### Contact Page (`contact.html`)
- Contact form with validation
- Company contact information
- Business hours and location
- FAQ section
- Social media links

## 🎨 Design Features

- **Color Scheme**: Professional blue gradient with white backgrounds
- **Typography**: Inter font family for modern readability
- **Animations**: Smooth fade-in effects and hover animations
- **Mobile-First**: Responsive design that works on all devices
- **Accessibility**: Proper semantic HTML and ARIA labels

## 🔧 Customization

### Changing Company Information
Edit the following files to update company details:
- `index.html` - Update hero text and company description
- `contact.html` - Update contact information and address
- `logo.jpeg` - Replace with your company logo

### Modifying Colors
Edit `styles.css` to change the color scheme:
- Primary color: `#007bff`
- Secondary color: `#0056b3`
- Gradient colors: `#667eea` to `#764ba2`

### Adding New Services
1. Edit `services.html` to add new service cards
2. Update the contact form dropdown in `contact.html`
3. Add corresponding FAQ entries in `electronics_company_faq.txt`

## 🚀 Deployment

### Local Development
- Use a local server (Python, Node.js, or any web server)
- Ensure the Streamlit chatbot is running on port 8501

### Production Deployment
1. **Static Hosting** (Netlify, Vercel, GitHub Pages):
   - Upload HTML, CSS, and JS files
   - Deploy Streamlit app separately (Streamlit Cloud, Heroku, etc.)
   - Update iframe src in `services.html` to point to deployed chatbot URL

2. **VPS/Server**:
   - Upload files to web server
   - Configure web server (Apache, Nginx)
   - Deploy Streamlit app on same server or separate instance

## 🔍 Troubleshooting

### Chatbot Not Loading
- Ensure Streamlit server is running on `http://localhost:8501`
- Check browser console for CORS errors
- Try using a local server instead of opening files directly

### Styling Issues
- Clear browser cache
- Check if all CSS files are loading properly
- Verify file paths are correct

### Form Not Working
- Check browser console for JavaScript errors
- Ensure `script.js` is properly loaded
- Verify form validation is working

## 📞 Support

For technical support or questions about the website:
- Email: support@pineapple.com
- Phone: +91 9876543210
- Business Hours: Mon–Sat, 9 AM to 8 PM

## 📄 License

This website is created for PINEAPPLE company. All rights reserved.

---

**Note**: Make sure to keep the Streamlit chatbot server running while testing the website, as the services page includes an embedded iframe that loads the chatbot interface. 