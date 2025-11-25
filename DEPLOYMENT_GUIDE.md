# 🚀 Deployment Guide - Email Productivity Agent

This guide provides step-by-step instructions for deploying your Email Productivity Agent to various hosting platforms.

## 🎯 Recommended: Streamlit Community Cloud (FREE)

**Best for**: Streamlit applications, easiest setup, zero cost

### Prerequisites
- GitHub account with your code pushed
- Google Gemini API key

### Step-by-Step Deployment

#### 1. Prepare Your Repository
Ensure your repository structure is correct:
```
oceanai/
└── email_agent/
    ├── app.py
    ├── requirements.txt
    ├── .gitignore
    ├── data/
    ├── models/
    ├── services/
    └── utils/
```

#### 2. Sign Up for Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Continue with GitHub"
3. Authorize Streamlit to access your GitHub account

#### 3. Deploy Your App
1. Click "New app" button
2. Fill in the deployment form:
   - **Repository**: `Harshgoyal2004/oceanai`
   - **Branch**: `main`
   - **Main file path**: `email_agent/app.py`
   - **App URL**: Choose a custom URL (e.g., `email-productivity-agent`)

#### 4. Configure Secrets (API Key)
1. Click "Advanced settings"
2. Go to "Secrets" section
3. Add your API key in TOML format:
   ```toml
   GEMINI_API_KEY = "your_actual_api_key_here"
   ```
4. Click "Save"

#### 5. Deploy!
1. Click "Deploy!" button
2. Wait for deployment (usually 2-5 minutes)
3. Your app will be live at: `https://your-app-name.streamlit.app`

#### 6. Verify Deployment
- [ ] App loads without errors
- [ ] Inbox displays correctly
- [ ] Process Inbox works
- [ ] Prompt Brain can edit prompts
- [ ] Email Agent chat responds
- [ ] No API key errors

### Troubleshooting Streamlit Cloud

**Issue**: App crashes on startup
- **Solution**: Check logs in Streamlit Cloud dashboard
- Verify `requirements.txt` has all dependencies
- Ensure API key is correctly set in secrets

**Issue**: "Module not found" error
- **Solution**: Add missing package to `requirements.txt`
- Redeploy the app

**Issue**: API key not working
- **Solution**: 
  - Check secrets are in correct TOML format
  - No quotes around the key name
  - Restart the app after updating secrets

---

## 🔧 Alternative: Render (FREE)

**Best for**: More control, supports multiple services

### Deployment Steps

#### 1. Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with GitHub

#### 2. Create Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Select `Harshgoyal2004/oceanai`

#### 3. Configure Service
```
Name: email-productivity-agent
Region: Choose closest to you
Branch: main
Root Directory: email_agent
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

#### 4. Add Environment Variables
1. Scroll to "Environment Variables"
2. Add:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your actual API key

#### 5. Select Plan
- Choose "Free" plan
- Click "Create Web Service"

#### 6. Wait for Deployment
- First deployment takes 5-10 minutes
- Monitor logs for any errors
- App will be live at: `https://email-productivity-agent.onrender.com`

### Render Limitations (Free Tier)
- App spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- 750 hours/month free

---

## 🚂 Alternative: Railway (FREE Tier)

**Best for**: Quick deployment, automatic detection

### Deployment Steps

#### 1. Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub

#### 2. Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `Harshgoyal2004/oceanai`

#### 3. Configure Settings
Railway auto-detects Python apps, but you may need to:
1. Click on your service
2. Go to "Settings"
3. Set:
   - **Root Directory**: `email_agent`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`

#### 4. Add Environment Variables
1. Go to "Variables" tab
2. Click "New Variable"
3. Add:
   - **Variable**: `GEMINI_API_KEY`
   - **Value**: Your API key

#### 5. Generate Domain
1. Go to "Settings"
2. Click "Generate Domain"
3. Your app will be at: `https://your-app.up.railway.app`

### Railway Limitations (Free Tier)
- $5 credit/month
- After credit exhausted, app stops
- Good for demos and testing

---

## 📝 Post-Deployment Checklist

After deploying to any platform:

### 1. Test All Features
- [ ] Load the deployment URL
- [ ] Verify inbox loads
- [ ] Test "Process Inbox" functionality
- [ ] Edit and save prompts in Prompt Brain
- [ ] Use Email Agent chat
- [ ] Check drafts page

### 2. Update Documentation
- [ ] Add deployment URL to README.md
- [ ] Update SUBMISSION_GUIDE.md with actual URL
- [ ] Commit and push changes

### 3. Share with Others
- [ ] Test URL in incognito/private browsing
- [ ] Verify it works on mobile devices
- [ ] Share with friends for feedback

---

## 🔒 Security Best Practices

### Never Commit API Keys
```bash
# Always verify .gitignore includes:
.env
.streamlit/secrets.toml
```

### Use Environment Variables
```python
# Good ✅
api_key = os.getenv("GEMINI_API_KEY")

# Bad ❌
api_key = "AIzaSy..."
```

### Rotate Keys if Exposed
If you accidentally commit an API key:
1. Immediately revoke it in Google Cloud Console
2. Generate a new key
3. Update deployment secrets
4. Remove from git history:
   ```bash
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch .env" \
   --prune-empty --tag-name-filter cat -- --all
   ```

---

## 📊 Monitoring Your Deployment

### Streamlit Cloud
- Dashboard: [share.streamlit.io/](https://share.streamlit.io/)
- View logs in real-time
- Monitor app health
- See usage analytics

### Render
- Dashboard: [dashboard.render.com](https://dashboard.render.com)
- View deployment logs
- Monitor resource usage
- Check uptime

### Railway
- Dashboard: [railway.app/dashboard](https://railway.app/dashboard)
- View logs and metrics
- Monitor credit usage
- Check deployment status

---

## 🆘 Common Deployment Issues

### Issue: Port Binding Error
**Symptoms**: App fails to start, port error in logs

**Solution**:
```python
# In app.py, ensure Streamlit uses environment port
import os
port = int(os.getenv("PORT", 8501))
```

**Start command**:
```bash
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

### Issue: File Not Found Errors
**Symptoms**: Can't load mock_inbox.json or prompts.json

**Solution**: Use relative paths from app.py location
```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INBOX_PATH = os.path.join(BASE_DIR, "data", "mock_inbox.json")
```

### Issue: Slow Cold Starts
**Symptoms**: First load takes 30+ seconds

**Solutions**:
- **Streamlit Cloud**: Always-on (no cold starts)
- **Render**: Upgrade to paid plan or accept delay
- **Railway**: Keep app active with uptime monitoring

### Issue: Out of Memory
**Symptoms**: App crashes randomly

**Solutions**:
- Optimize data loading
- Clear session state when not needed
- Use pagination for large datasets
- Upgrade to paid tier with more RAM

---

## 🎓 Deployment Comparison

| Feature | Streamlit Cloud | Render | Railway |
|---------|----------------|---------|----------|
| **Cost** | Free forever | Free tier | $5/month credit |
| **Cold Starts** | None | Yes (15 min) | Minimal |
| **Setup Difficulty** | ⭐ Easy | ⭐⭐ Medium | ⭐⭐ Medium |
| **Custom Domain** | ❌ No | ✅ Yes | ✅ Yes |
| **Best For** | Streamlit apps | Any Python app | Quick deploys |
| **Limitations** | Streamlit only | Spins down | Credit limit |

**Recommendation**: Use **Streamlit Cloud** for this project - it's designed for Streamlit apps and has the easiest setup.

---

## ✅ Final Deployment Verification

Before submitting, verify:

```bash
# 1. Test deployment URL
curl https://your-app.streamlit.app

# 2. Check all pages load
# Visit each page in browser:
# - Inbox
# - Prompt Brain  
# - Email Agent
# - Drafts

# 3. Test functionality
# - Process inbox
# - Edit prompts
# - Chat with agent
# - View drafts

# 4. Check logs for errors
# Review platform dashboard logs

# 5. Test from different devices
# - Desktop browser
# - Mobile browser
# - Incognito mode
```

---

## 📞 Support Resources

- **Streamlit**: [docs.streamlit.io](https://docs.streamlit.io)
- **Streamlit Community**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **Render Docs**: [render.com/docs](https://render.com/docs)
- **Railway Docs**: [docs.railway.app](https://docs.railway.app)

---

## 🎉 Success!

Once deployed, your app is live and accessible worldwide! 🌍

Remember to:
1. Add the URL to your README.md
2. Include it in your video demo
3. Test it thoroughly before submission
4. Keep your API key secure

Good luck with your submission! 🚀
