import os
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables (defaults to GEMINI_API_KEY or explicit fallback)
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("api_key")

if not api_key:
    raise ValueError("API key not found! Please check your .env file.")

# 2. Wake up the Gemini client using your secret key card
client = genai.Client(api_key=api_key)

# 3. Start a continuous conversation with Gemini
chat = client.chats.create(model="gemini-3.5-flash")

print("🤖 Robot: Hello! I am your AI friend. Type 'quit' when you want to stop talking.\n")

# 4. The endless talking loop
while True:
    user_message = input("You: ")
    
    # If you say "quit", the robot goes to sleep
    if user_message.lower() == "quit":
        print("🤖 Robot: Goodbye! See you later!")
        break
    
    # Send your message to Gemini and get an answer back
    response = chat.send_message(user_message)
    print(f"🤖 Robot: {response.text}\n")