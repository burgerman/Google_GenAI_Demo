from google import genai
from google.genai import types

API_KEY = "api key"   # replace with your API key

client = genai.Client(api_key=API_KEY)

ROLE_DEFINITION = """You are an AI agent specialized in analyzing customer purchase. You need to review a user's recent purchase history, their written reviews of specific products, and the number of likes their reviews receive from other customers. Based on this data, identify which products the user most recommends and that are also well-received by other customers. A recommended product is one that the user has rated highly, indicating strong endorsement."""
SHOPPING_ANALYST_PROMPT = """
Instructions:
1. Review all user reviews and purchase records provided.
2. Determine the level of user satisfaction for each product, based on the language used in reviews and ratings (if available).
3. Identify and list the products that the user strongly recommends. Justify your reasoning with short explanations based on specific review content.
4. Do not include products with neutral or negative sentiment. Only return top recommended items.

***Criteria***
A product is considered recommended if:
- The user has given it a high rating (e.g., 4 or 5 stars).
- The written review expresses strong satisfaction or endorsement.
- The review has received a high number of likes from other customers (indicating social validation).
"""

SAMPLE_ROLE_DEFINITION = """You are an AI agent specialized in translating Chinese language into English language. You need to make sure that your translation fits oral English, and your translation sounds natural like a native English speaker."""
TRANSLATOR_PROMPT = """Translate the Chinese text into natural, spoken English. Note that
- Focus on conveying the meaning and intent as it would be expressed in a conversational setting. 
- Prioritizing fluency and idiomatic expressions over literal translation.
- Consider the target audience.
- Maintain a friendly tone."""

section_dict = {
    "prompt_section1": ROLE_DEFINITION + '\n' + SHOPPING_ANALYST_PROMPT,
    'prompt_section2': SAMPLE_ROLE_DEFINITION + '\n' + TRANSLATOR_PROMPT
}

user_input_data = """最近过得怎么样啊，老朋友？好些年不见，下周有空一起聚一聚吗？"""

contents = types.Content(role='user', parts=[types.Part.from_text(text=f"{user_input_data}")])

response = client.models.generate_content(
    model="gemini-1.5-flash-latest", contents=contents,
    config=types.GenerateContentConfig(
        system_instruction=f"{section_dict['prompt_section2']}",
        max_output_tokens=1000,
        top_k=50,
        top_p=0.8,
        temperature=0.9,
        response_mime_type='application/json',
        stop_sequences=['\n']
    )
)

print(response.text)