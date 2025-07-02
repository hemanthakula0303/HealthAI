import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("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"))

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
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": question}
                ]
            )
            print("AI:", response.choices[0].message.content)
        except Exception as e:
            print("❌ Error:", e)