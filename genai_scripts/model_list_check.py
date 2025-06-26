from google import genai
from google.genai import types

API_KEY = "AIzaSyDK19UnJoC283B3w-_kaa1o9CfoExaJrbg"   # replace with your API key
# API_KEY = "AIzaSyACH8BV1h1WscmMcbv6wXygmpBm_Z--yIE"

client = genai.Client(api_key=API_KEY)
for model in client.models.list():
    print(model.name)