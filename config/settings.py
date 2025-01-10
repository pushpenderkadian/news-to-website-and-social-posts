import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# API keys and credentials
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
STABILITY_AI_API_KEY = os.getenv("STABILITY_AI_API_KEY")


# Social media credentials

META_ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
INSTAGRAM_USERID = os.getenv("INSTAGRAM_USERID")

# Other settings
RSS_FEED_URL = os.getenv("RSS_FEED_URL")
RSS_FEED_COUNT = 1  # Number of feeds to fetch (0 for all)
IMAGE_OUTPUT_DIR = "static/uploads"

# MongoDB settings
MGDB=os.getenv("MGDB")