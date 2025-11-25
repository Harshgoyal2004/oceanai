# 📋 Project Submission Guide

This guide will help you prepare your **Email Productivity Agent** project for submission.

## ✅ Submission Requirements Checklist

### 1. GitHub Repository ✓
- [x] Repository initialized and connected: `https://github.com/Harshgoyal2004/oceanai.git`
- [ ] All code committed and pushed
- [ ] README.md is comprehensive
- [ ] .gitignore properly configured
- [ ] No sensitive data (API keys) in repository

### 2. Video Demo (Max 15 Minutes) 📹
- [ ] Record video demonstration
- [ ] Upload to Google Drive
- [ ] Set sharing permissions to "Anyone with the link"
- [ ] Add video link to README.md

### 3. Deployment (Bonus) 🚀
- [ ] Deploy application to hosting platform
- [ ] Add deployment URL to README.md

---

## 📝 Video Demo Script (15-Minute Structure)

### Introduction (1 minute)
- Introduce yourself
- Project name and purpose
- Brief overview of features

### Code Walkthrough (6 minutes)
**Project Structure (2 min)**
- Explain folder organization (`app.py`, `services/`, `models/`, `data/`)
- Show key files and their purposes

**Core Components (4 min)**
- **Prompt-Driven Architecture**: Show `data/prompts.json` and how prompts control agent behavior
- **LLM Integration**: Explain `services/llm_service.py` and Gemini API usage
- **Email Processing**: Walk through `services/email_processor.py`
- **Streamlit UI**: Highlight `app.py` structure

### Live Demo (6 minutes)
1. **Setup & Launch** (1 min)
   - Show `.env` configuration (blur API key)
   - Run `streamlit run app.py`

2. **Feature Demonstration** (5 min)
   - **Inbox View**: Show mock inbox loading
   - **Process Inbox**: Click "Process Inbox" button, show categorization and action items
   - **Prompt Brain**: Navigate to Prompt Brain, edit a prompt, save it
   - **Email Agent Chat**: Ask questions like:
     - "Summarize the email from John"
     - "Draft a reply to the meeting request"
   - **Drafts**: Show generated drafts

### Approach & Workflow (2 minutes)
- Development approach (prompt-driven design)
- Challenges faced and solutions
- Technology stack (Streamlit, Google Gemini, Python)
- Testing methodology

### Conclusion (30 seconds)
- Summary of achievements
- Future enhancements
- Thank you

---

## 🎥 Video Recording Tips

### Tools You Can Use
- **macOS**: QuickTime Player (built-in screen recording)
- **Cross-platform**: OBS Studio (free), Loom, Zoom
- **Chrome Extension**: Loom, Screencastify

### Recording Best Practices
1. **Preparation**
   - Close unnecessary applications
   - Clear browser tabs
   - Prepare a script or outline
   - Test audio before recording

2. **During Recording**
   - Speak clearly and at moderate pace
   - Use cursor to highlight important code sections
   - Zoom in on code when explaining details
   - Show terminal commands and outputs

3. **Quality Settings**
   - Resolution: 1080p (1920x1080) minimum
   - Frame rate: 30 fps
   - Audio: Clear microphone (test beforehand)

4. **File Management**
   - Keep video under 15 minutes
   - Export in MP4 format for compatibility
   - File size: Compress if over 2GB for easier upload

---

## ☁️ Google Drive Upload Instructions

1. **Upload Video**
   ```
   - Go to drive.google.com
   - Click "New" → "File upload"
   - Select your video file
   - Wait for upload to complete
   ```

2. **Set Sharing Permissions**
   ```
   - Right-click on uploaded video
   - Click "Share"
   - Change to "Anyone with the link"
   - Set permission to "Viewer"
   - Copy the link
   ```

3. **Add Link to README**
   - Update your README.md with the video link
   - Commit and push changes

---

## 🚀 Deployment Options (Bonus)

### Option 1: Streamlit Community Cloud (Recommended - FREE)

**Pros**: Free, easy, designed for Streamlit apps
**Steps**:
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `Harshgoyal2004/oceanai`
5. Set main file path: `email_agent/app.py`
6. Add secrets (API key) in "Advanced settings" → "Secrets":
   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```
7. Click "Deploy"

### Option 2: Render (FREE)

**Steps**:
1. Go to [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New" → "Web Service"
4. Connect your repository
5. Configure:
   - **Name**: email-productivity-agent
   - **Root Directory**: `email_agent`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variable: `GEMINI_API_KEY`
7. Click "Create Web Service"

### Option 3: Railway (FREE Tier)

**Steps**:
1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add environment variable: `GEMINI_API_KEY`
6. Railway will auto-detect and deploy

---

## 📦 Pre-Submission Checklist

### Code Quality
- [ ] All code is properly commented
- [ ] No hardcoded API keys (use .env)
- [ ] Requirements.txt is up to date
- [ ] Code follows Python best practices (PEP 8)

### Documentation
- [ ] README.md includes:
  - [ ] Project description
  - [ ] Features list
  - [ ] Setup instructions
  - [ ] Usage guide
  - [ ] Video demo link
  - [ ] Deployment URL (if applicable)
- [ ] Code has docstrings for main functions

### Repository
- [ ] All changes committed
- [ ] All commits pushed to GitHub
- [ ] Repository is public (or accessible to evaluators)
- [ ] .gitignore excludes sensitive files

### Testing
- [ ] Application runs without errors
- [ ] All features work as expected
- [ ] Mock inbox loads correctly
- [ ] Prompts can be edited and saved
- [ ] Chat functionality works

---

## 🔍 Final Verification Steps

1. **Clone Fresh Copy**
   ```bash
   cd /tmp
   git clone https://github.com/Harshgoyal2004/oceanai.git
   cd oceanai/email_agent
   ```

2. **Test Setup**
   ```bash
   pip install -r requirements.txt
   # Create .env with API key
   streamlit run app.py
   ```

3. **Verify All Features**
   - Load inbox
   - Process emails
   - Edit prompts
   - Use chat
   - View drafts

4. **Check Video**
   - Watch your video completely
   - Verify audio quality
   - Confirm duration ≤ 15 minutes
   - Test Google Drive link access (incognito mode)

---

## 📤 Submission Format

When submitting, provide:

1. **GitHub Repository URL**
   ```
   https://github.com/Harshgoyal2004/oceanai
   ```

2. **Video Demo Link**
   ```
   https://drive.google.com/file/d/YOUR_FILE_ID/view?usp=sharing
   ```

3. **Deployment URL** (if applicable)
   ```
   https://your-app-name.streamlit.app
   ```

---

## 💡 Quick Commands Reference

```bash
# Check git status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Final submission preparation"

# Push to GitHub
git push origin main

# Run application locally
streamlit run app.py

# Test in fresh environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 🆘 Troubleshooting

### Video Too Large for Google Drive
- Compress using HandBrake or online tools
- Reduce resolution to 720p if needed
- Use H.264 codec for better compression

### Deployment Fails
- Check logs for errors
- Verify requirements.txt includes all dependencies
- Ensure API key is set in environment variables
- Check if port configuration is correct

### Application Won't Run
- Verify Python version (3.8+)
- Check all dependencies installed
- Ensure .env file exists with valid API key
- Check file paths are correct

---

## ✨ Good Luck!

Remember:
- **Quality over quantity** in your video
- **Test everything** before submission
- **Double-check** all links work
- **Submit before deadline**

If you need help, refer to:
- [Streamlit Documentation](https://docs.streamlit.io)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- Your project README.md
