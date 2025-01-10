import requests,datetime
from config.settings import STABILITY_AI_API_KEY,IMAGE_OUTPUT_DIR

def generate_image(prompt):
    APIURL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "authorization": f"Bearer {STABILITY_AI_API_KEY}",
        "accept": "image/*"
    }
    data = {
        "prompt": prompt,
        "output_format": "jpeg"
    }

    # Sent in this way because the API expects Multipart form data
    response = requests.post(APIURL,headers=headers,files={"none": ''},data=data)
    if response.status_code != 200:
        raise Exception(f"Failed to generate image: {response.text}")
    else:
        image_path = f"{IMAGE_OUTPUT_DIR}/gen_image_{int(datetime.datetime.now().timestamp())}.jpeg"
        with open(image_path, "wb") as file:
            file.write(response.content)
        return image_path
