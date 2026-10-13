import datetime
import os
from langchain.chat_models import init_chat_model 
from langchain.tools import Tool, tool
from dotenv import load_dotenv
load_dotenv() 

llm = init_chat_model(
    model=os.getenv(key="MODEL_NAME"),  
    temperature=1.0,
    api_key=os.getenv(key="API_KEY")
)
@tool
def get_time():
    """Returns the current time as a string in the format 'YYYY-MM-DD HH:MM:SS'."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

SYSTEM_PROMPT = "You are a helpful AI assistant!"
history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

#question = input("You: ")
#response = llm.invoke(input=question)
#print(f"Bot: {response.content}")

print("Welcome to Cue chat")
while True:
    question = input("You: ").strip()

    if not question:
        continue
    if question.lower() in ("exit", "quit", "bye"):
        print("Goodbye!")
        break

    history.append({"role": "user", "content": question})

    full = None
    for chunk in llm.stream(input=history):
        full = chunk if full is None else full + chunk
        print(full.text)

  
    history.append(full)

    print(f"Bot: {full.content}")