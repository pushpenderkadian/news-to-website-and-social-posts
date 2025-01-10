import feedparser
from config.settings import RSS_FEED_URL, RSS_FEED_COUNT
from database import db


def fetch_latest_rss_feed():
    feed = feedparser.parse(RSS_FEED_URL)
    if RSS_FEED_COUNT:
        feed.entries = feed.entries[:RSS_FEED_COUNT]
    new_feed = []
    for entry in feed.entries:
        if check_feed_exitance_in_db(entry):
            break
        latest_entry = entry  # Get the most recent article
        new_feed.append({
            "title": latest_entry.title,
            "link": latest_entry.link,
            "summary": latest_entry.summary,
            "post_id": latest_entry["post-id"]
        })
    return new_feed

def check_feed_exitance_in_db(feed_item):
    if db.feeds.find_one({"post_id": feed_item["post-id"]}):
        return True
    else:
        return False