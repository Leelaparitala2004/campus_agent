from huggingface_hub import InferenceClient
import os

client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))

response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ],
    max_tokens=200
)

print(response.choices[0].message["content"])
