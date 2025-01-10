import requests
from config.settings import INSTAGRAM_USERID, META_ACCESS_TOKEN

# Instagram do not support local image upload so it should be hosted somewhere and the should be publically accessible
def post_to_instagram(image_path, caption):
    url_initialize_post = f"https://graph.facebook.com/v19.0/{INSTAGRAM_USERID}/media?caption={caption}&image_url={image_path}&origin_graph_explorer=1&transport=cors&access_token={META_ACCESS_TOKEN}"
    
    response = requests.post(url_initialize_post)
    if response.status_code != 200:
        raise Exception(f"Failed to post to Instagram: {response.text}")
    else:
        data=response.json()
        creation_id=data["id"]

        url_publish_post = f"https://graph.facebook.com/v19.0/{INSTAGRAM_USERID}/media_publish?creation_id={creation_id}&access_token={META_ACCESS_TOKEN}"
        response = requests.post(url_publish_post)
        if response.status_code != 200:
            raise Exception(f"Failed to publish post: {response.text}")
        else:
            return response.json()
    

