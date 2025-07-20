import os
from dotenv import load_dotenv
from together import Together

# Load the API key from .env
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Initialize Together AI client
client = Together(api_key=api_key)

def ask_ai():
    print("\n🤖 Ask HealthAI (type 'exit' to go back)")

    while True:
        question = input("You: ")

        if question.lower() == "exit":
            print("👋 Exiting chat.")
            break

        if not question.strip():
            print("⚠ Please enter a valid question.")
            continue

        try:
            response = client.chat.completions.create(
                model="deepseek-ai/DeepSeek-V3",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant specialized in healthcare."},
                    {"role": "user", "content": question}
                ]
            )
            print("AI:", response.choices[0].message.content.strip())
        except Exception as e:
            print("❌ Error:", e)
