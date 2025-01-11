# variety.com Feed Automation Project

## Overview
This project automates fetching RSS feed items, processing them, and posting to Instagram. It uses various APIs, including Stability AI, OpenAI, and Hugging Face for content generation and enhancements. A FastAPI web application provides a frontend for viewing the feeds (Word Press can also be used). Most of the APIs and everything used are completly free to use or have freemium packages.

### Key Features:
- Fetch RSS feeds and store them in MongoDB to display on the website.
- Generate captions for RSS feed articles using OpenAI and Hugging Face APIs.
- Generate AI-based images for articles using Stability AI.
- Shorten URLs using Pyshorteners.
- Post to Instagram via Meta Graph API.
- Display processed feeds on a FastAPI web interface.

---

## Installation

### Prerequisites
1. **Python**: Install Python 3.8 or later.
2. **MongoDB**: Ensure MongoDB is installed and running or hosted over mongo server.
3. **Ngrok**: Install Ngrok for exposing the app to the internet.
4. **API Keys**:
   - Stability AI
   - OpenAI
   - Hugging Face
   - Meta Graph API (for Instagram posting)

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/pushpenderkadian/news-to-website-and-social-posts
   cd news-to-website-and-social-posts
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Fill in the required API keys and MongoDB URI in the `.env` file:
     ```env
     STABILITY_AI_API_KEY=<your_stability_ai_api_key>
     OPENAI_API_KEY=<your_openai_api_key>
     HUGGINGFACE_API_KEY=<your_huggingface_api_key>
     META_ACCESS_TOKEN=<your_meta_access_token>
     INSTAGRAM_USERID=<your_instagram_user_id>
     RSS_FEED_URL=<your_rss_feed_url>
     MGDB=<your_mongo_db_connection_string>
     ```

4. **Prepare Database:**
   Initialize the MongoDB database:
   ```python
   from database import initialize_db
   initialize_db()
   ```

5. **Run the Application:**
   ```bash
   python app.py
   ```
   This will:
   - Start the FastAPI server.
   - Start a background task for fetching feeds.
   - Provide an Ngrok URL for public access.

6. **Access the Application:**
   Use the Ngrok public URL printed in the console to access the web interface.

---

## File Structure

```
project/
|-- app/
|   |-- utils/
|       |-- rss_fetcher.py  # Fetches RSS feeds.
|       |-- stability_ai.py # Generates images using Stability AI.
|       |-- text_processor.py # Processes text using OpenAI and Hugging Face.
|       |-- url_shortener.py # Shortens URLs.
|   |-- feed_processor.py    # Processes and combines feed data with ai generated caption and images.
|-- config/
|   |-- settings.py          # Loads environment variables.
|-- social_media/
|   |-- instagram_post.py    # Posts content to Instagram.
|-- static/uploads/          # Directory for ai generated images.
|-- templates/index.html     # Frontend for displaying feeds.
|-- database.py              # MongoDB integration.
|-- app.py                   # Main application entry point.
|-- requirements.txt         # Python dependencies.
|-- .env.example             # Sample environment variables.
```

---

## Generating API Keys

### Stability AI
1. Visit [Stability AI Developer Portal](https://platform.stability.ai/).
2. Sign up or log in.
3. Click on the profile icon in top right corner and Navigate to API Keys to generate a new key.
4. Add the key to `.env`:
   ```env
   STABILITY_AI_API_KEY=<your_stability_ai_api_key>
   ```

### OpenAI
1. Visit [OpenAI API](https://platform.openai.com/).
2. Sign up or log in.
3. Generate an API key under your account settings.
4. Add the key to `.env`:
   ```env
   OPENAI_API_KEY=<your_openai_api_key>
   ```

### Hugging Face
1. Visit [Hugging Face](https://huggingface.co/).
2. Sign up or log in.
3. Go to Your Profile Settings:
    A. Click on your profile picture or username in the top-right corner.
    B. Select "Settings" from the dropdown menu.
4. Navigate to Access Tokens:
    A. In the left-hand menu, click "Access Tokens".
    B. Create an API Token:
    C. Click "New Token" and give it a name (e.g., "My Project").
    D. Choose the appropriate role (Read is sufficient for most API use cases).
    E. Click "Generate Token".
5. Copy Your API Key
6. Add the key to `.env`:
   ```env
   HUGGINGFACE_API_KEY=<your_huggingface_api_key>
   ```

### Meta Graph API (Instagram)
1. Visit [Meta for Developers](https://developers.facebook.com/).
2. Create a new app and enable Instagram Graph API.
3. Generate an access token for Instagram and retrieve your Instagram user ID.
4. You can refer this video for generating User tokens and Instagram UsedID https://www.youtube.com/watch?v=BuF9g9_QC04
4. Add the details to `.env`:
   ```env
   META_ACCESS_TOKEN=<your_meta_access_token>
   INSTAGRAM_USERID=<your_instagram_user_id>
   ```


### NGROK Setup
1. Visit [NGROK Website](https://dashboard.ngrok.com/).
2. Sign up or log in.
3. from left menu goto Your Authtoken and copy your token
4. Add the key to `.env`:
   ```env
   NGROK_AUTH_TOKEN=<your_NGROK_Auth_key>
---

## Usage

1. **Fetching and Processing Feeds:**
   - Feeds are fetched every hour via the background task `cron_for_fetching_feeds()`.
   - New feeds are processed, captions and images are generated, and content is saved to the database.

2. **Viewing Feeds:**
   - Open the Ngrok URL in your browser to view the processed feeds.

3. **Posting to Instagram:**
   - Images and captions are automatically posted to Instagram during feed processing.

---

## Notes

- Ensure the `static/uploads/` directory exists and is writable for storing AI-generated images.
- Instagram API requires hosted images. Ngrok's public URL is used for hosting generated images temporarily.

---

## Troubleshooting

### Common Issues:

1. **API Key Errors:**
   - Double-check API keys in the `.env` file.
   - Ensure keys are active and have sufficient permissions.

2. **MongoDB Connection Errors:**
   - Verify the MongoDB URI in the `.env` file.
   - Ensure MongoDB is running and accessible.

3. **Ngrok Issues:**
   - Ensure Ngrok is installed and accessible via the `ngrok` command.


---
