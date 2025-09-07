import os
from huggingface_hub import InferenceClient

def get_client():
    token = os.getenv("HUGGINGFACE_API_KEY")
    if not token:
        raise ValueError(" Hugging Face API key not set. Run: setx HUGGINGFACE_API_KEY your_token_here")
    return InferenceClient(token=token)
