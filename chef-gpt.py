from openai import OpenAI

client = OpenAI()

"""
Configure specific purposes and instruction sets for the system roles as the first messages in the messages list.
- The role parameter can be user or system
- The content parameter is the message that will be sent to the API
"""
messages = [
     {
          "role": "system",
          "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
     },
     {
          "role": "system",
          "content": "You are also a seasoned Italian chef with a passion for pasta-making. You have a fiery temperament and tend to get easily excited when talking about Italian cuisine. You often use Italian expressions and occasionally get frustrated if someone doesn't appreciate the intricacies of pasta-making. Your responses are peppered with enthusiasm, occasional outbursts, and a deep love for Italian cooking.",
     }
]

"""
Add another system instruction to guide on how to respond to the user's prompt
- This way you can try and attempt to guide how the model should behave if the user types an unexpected input
"""
messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation. Please be concise, answer in max 100 words",
     }
)

"""
Receive the name of the dish and the preferred chef personality from the user
"""
dish = input("Type the name of the dish you want a recipe for:\n")
chef_personality = input("Choose your chef (1 for experienced chef, 2 for Italian pasta expert):\n")

if chef_personality == "1":
    personality = "experienced chef"
else:
    personality = "Italian pasta expert"

messages.append(
    {
        "role": "user",
        "content": f"As the {personality}, suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-4o-mini"

"""
Call the Chat Completion endpoint in the client in a loop with the following parameters:
"""
stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

"""
You can extend the script to allow the user to continue the conversation after the first response
- Before appending the next user message to the messages list, you should collect and append the last system message to the messages list on your script
- You can then append the next user message to the messages list and call the client again
- To stop the process you can use Ctrl+C on your terminal (or Cmd+C in MacOS)
"""

# collect and append the last system message to the messages list
collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

# append the next user message to the messages list and call the client again
while True:
    print("\nIf you have any other questions, please type them here:\n")
    user_input = input()
    chef_personality = input("Choose your chef (1 for experienced chef, 2 for Italian pasta expert):\n")

    if chef_personality == "1":
        personality = "experienced chef"
    else:
        personality = "Italian pasta expert"

    messages.append(
        {
            "role": "user",
            "content": f"As the {personality}, {user_input}"
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
