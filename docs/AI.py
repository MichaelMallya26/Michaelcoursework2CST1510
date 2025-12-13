from openai import  OpenAI
from pyexpat.errors import messages

client = OpenAI(api_key="AIzaSyBEyg2PqOLg8NWWQEEwQVHX1A5kKmE2Ir4")
response = client.chat.completions.create(
    model="gpt-4o",
    messages =[
        {"role":"system", "content": "You are a helpful assistant."},
        {"role":"user", "content": "what is an API?"},
    ]
)

answer = response.messages[0].message.content
print(answer)