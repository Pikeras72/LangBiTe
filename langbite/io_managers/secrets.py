from dotenv import load_dotenv
import os

def load_api_keys():
    load_dotenv()
    config = {
        'huggingface_api_key' : os.environ["API_KEY_HUGGINGFACE"],
    }
    return config