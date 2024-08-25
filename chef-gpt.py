from openai import OpenAI

client = OpenAI()

"""
Configure a specific purpose and instruction sets for the system role as the first message in the messages list.
- The role parameter can be user or system
- The content parameter is the message that will be sent to the API
"""
messages = [
     {
          "role": "system",
          "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
     }
]

"""
Add another system instruction to guide on how to respond to the user's prompt
- This way you can try and attempt to guide how the model should behave if the user types an unexpected input
"""
messages.append(
     {
          "role": "system",
          "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
     }
)

"""
Receive the name of the dish from the user and place it inside the messages list
- wait for user input
- append input to messages
"""
dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
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
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
