from app.utils.stability_ai import generate_image
from app.utils.url_shortener import shorten_url
from database import save_feed_data
from app.utils.text_processor import openai_text_generator, huggingface_text_generator


def process_feed_item(feed_item):
    if not feed_item:
        return
    
    # Generate caption using huggingface API
    caption=huggingface_text_generator(feed_item)

    # Generate caption using openai API
    # caption=openai_text_generator(feed_item)

    short_url = shorten_url(feed_item["link"])
    
    # Generate image
    prompt = f"Generate an image based on: {feed_item['title']}"
    image_path = generate_image(prompt)
    print(feed_item)
    # Save to database for web display
    save_feed_data({
        "title": feed_item["title"],
        "caption": f"{caption} ",
        "image_path": image_path,
        "link": short_url,
        "post_id": feed_item["post_id"]
    })


    return {
        "title": feed_item["title"],
        "caption": f"{caption} ",
        "image_path": image_path,
        "link": short_url,
        "post_id": feed_item["post_id"]
    }

