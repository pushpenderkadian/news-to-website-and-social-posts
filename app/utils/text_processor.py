import requests
from config.settings import OPENAI_API_KEY, HUGGINGFACE_API_KEY

def openai_text_generator(feed_item):
    API_URL = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization":f"Bearer {OPENAI_API_KEY}"}
    data={
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"Write a 2-3 sentence caption for the following article: {feed_item['title']} - {feed_item['summary']}"}],
        "temperature": 0.1,
        "max_tokens": 60
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code != 200:
        raise Exception(f"Failed to generate caption: {response.text}")
    caption = response.json()["choices"][0]["message"]["content"]
    return caption

def huggingface_text_generator(feed_item):
    API_URL = "https://api-inference.huggingface.co/models/bigscience/mt0-large"
    # API_URL="https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    caption_response = requests.post(API_URL, headers=headers, json={"inputs": f"Write a 2-3 sentence caption for the following article: {feed_item['title']} - {feed_item['summary']}","parameters": {"max_length": 50}},timeout=300)
    if caption_response.status_code != 200:
        raise Exception(f"Failed to generate caption: {caption_response.text}")
    else:
        caption_response = caption_response.json()
        caption = caption_response[0]["generated_text"]
        return caption
