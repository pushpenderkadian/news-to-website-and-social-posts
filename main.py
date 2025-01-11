from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import initialize_db
from app.utils.rss_fetcher import fetch_latest_rss_feed
from app.feed_processor import process_feed_item
from social_media.instagram_post import post_to_instagram
from pyngrok import ngrok
import threading, time, uvicorn
from config.settings import NGROK_AUTH_TOKEN


app = FastAPI()


# Static files and templates 
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize the database
initialize_db()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    from database import get_all_feed_data
    data = get_all_feed_data()
    return templates.TemplateResponse("index.html", {"request": request, "feeds": data})


# Background task to fetch feeds periodically then put into the database and post to Instagram
def cron_for_fetching_feeds():
    while True:
        new_feed = fetch_latest_rss_feed()
        for feed_item in new_feed:
            feed_data=process_feed_item(feed_item)
            post_to_instagram(ngrok_url+"/"+feed_data["image_path"], feed_data["caption"])
        time.sleep(3600)



if __name__ == "__main__" :

    # Start ngrok
    global ngrok_url
    ngrok.set_auth_token(NGROK_AUTH_TOKEN)
    ngrok_url = ngrok.connect(8000).public_url
    print("Public URL to access the app:", ngrok_url)

    thread = threading.Thread(target=cron_for_fetching_feeds, daemon=True)
    thread.start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
