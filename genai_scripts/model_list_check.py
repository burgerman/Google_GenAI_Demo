from google import genai
from google.genai import types

API_KEY = ""   # replace with your API key

client = genai.Client(api_key=API_KEY)
for model in client.models.list():
    print(model.name)
