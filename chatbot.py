import os
from groq import Groq
from datetime import datetime

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def save_message(file, role, message):
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{role}: {message}\n")

def chat():
    print("🤖 Ak Bot - Your Personal AI Assistant")
    print("Type 'quit' to exit\n")

    # Create a new chat history file with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    history_file = f"chat_{timestamp}.txt"

    print(f"💾 Chat will be saved to: {history_file}\n")

    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye! 👋")
            save_message(history_file, "Bot", "Goodbye! 👋")
            print(f"\n✅ Chat saved to {history_file}")
            break

        if not user_input:
            continue

        # Save user message
        save_message(history_file, "You", user_input)

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are Ak Bot, a helpful and friendly personal AI assistant."},
                *conversation_history
            ],
            max_tokens=1024
        )

        assistant_reply = response.choices[0].message.content

        # Save bot reply
        save_message(history_file, "Bot", assistant_reply)

        conversation_history.append({
            "role": "assistant",
            "content": assistant_reply
        })

        print(f"Ak Bot: {assistant_reply}\n")

if __name__ == "__main__":
    chat()