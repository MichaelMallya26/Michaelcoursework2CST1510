from google import genai
from openai import api_key
from pyexpat.errors import messages

api_key ='AIzaSyBEyg2PqOLg8NWWQEEwQVHX1A5kKmE2Ir4'



client = genai.Client(api_key=api_key)

messages = [{"role": "user", "parts":[{"text": "Your name is Michael"}]}]

while True:
    user_input = input("YOU: ")
    if user_input.lower() == 'quit':
        print("Goodbye")
        break
    messages.append({"role": "user", "parts":[{"text": user_input}]})
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents= messages
    )
    print("AI: ", end="")
    full_reply =""
    for chunk in response:
        full_reply += chunk.text
        print(full_reply, end="")
        print("")
    messages.append({"role": "user", "parts":[{"text": full_reply}]})

