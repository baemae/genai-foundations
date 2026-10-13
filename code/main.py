import os
from langchain.chat_models import init_chat_model

from dotenv import load_dotenv

load_dotenv()

# raise exception if MODEL_NAME is not set
model_name = os.getenv(key="MODEL_NAME")
if not model_name:
    raise SystemError("MODEL_NAME is not set in the .env file.")

llm = init_chat_model(
    model=os.getenv(key="MODEL_NAME"),
    api_key=os.getenv(key="API_KEY"),
)

SYSTEM_PROMPT = "You are a helpful AI assistant!"
history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# question = input("You: ")
# response = llm.invoke(input=question)
# print(f"Bot: {response.content}")

print("Welcome to Cue chat")
while True:
    try:
        question = input("You: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break

    if not question:
        continue
    if question.lower() in ("exit", "quit", "bye"):
        print("Goodbye!")
        break

    history.append({"role": "user", "content": question})
    print("Bot: ", end="", flush=True)
    full = None
    completed = True
    try:
        for chunk in llm.stream(input=history):
            print(chunk.text, end="", flush=True)
            full = chunk if full is None else full + chunk
        print()
        completed = True

        if full is not None and full.text:
            history.append({"role": "assistant", "content": full.content})
    except KeyboardInterrupt:
        print("\n[interrupted]")
        history.pop()
    except Exception as e:
        print(f"\n[error: {e}]")
        history.pop() #discard user msg if it fails
