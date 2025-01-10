from pymongo import MongoClient
from config.settings import MGDB

client = MongoClient(MGDB)
db = client["rss_feed_project"]

def initialize_db():
    db.feeds.create_index("post_id", unique=True)

def save_feed_data(data):
    try:
        db.feeds.insert_one(data)
    except Exception as e:
        print("Duplicate or Error:", e)

def get_all_feed_data():
    return list(db.feeds.find({}, {"_id": 0}))
