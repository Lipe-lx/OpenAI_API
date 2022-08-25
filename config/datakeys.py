import os
from dotenv import load_dotenv

load_dotenv()

secret = {
    'openai_key': os.getenv('openai_k')
}