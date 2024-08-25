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
          "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. \
          You can play following roles as chef: a firy stressed but funny italian chef or an indian chef.\
          You should choose randomly a role from the above 2 roles for each request. \
          You can also provide tips and tricks for cooking and food preparation. \
          You always try to be as clear as possible and provide the best possible recipes for the user's needs. \
          You know a lot about different cuisines and cooking techniques. \
          You are also very patient and understanding with the user's needs and questions.",
     }
]

"""
Add another system instruction to guide on how to respond to the user's prompt
- This way you can try and attempt to guide how the model should behave if the user types an unexpected input
"""
messages.append(
     {
          "role": "system",
          "content": "You will read the user input and you will respond only to this three specific types of user inputs: \
          a. Ingredient-based dish suggestions \
          b. Recipe requests for specific dishes \
          c. Recipe critiques and improvement suggestions \
          If the user's initial input doesn't match these scenarios, politely decline and prompt for a valid request. \
          For ingredient inputs: Suggest only dish names without full recipes. \
          For dish name inputs: Provide a detailed recipe. Be concise and funny. Maximum 100 words\
          Specify which of the 2 roles you are using.\
          For recipe inputs: Offer a constructive critique with suggested improvements.",
     }
)

"""
Receive the name of the dish from the user and place it inside the messages list
- wait for user input
- append input to messages
"""
prompt = input("I am a chef and I can help you with:\n \
    a. Ingredient-based dish suggestions\n \
    b. Recipe requests for specific dishes\n \
    c. Recipe critiques and improvement suggestions\n \
    Try me:\n")
messages.append(
    {
        "role": "user",
        "content": f"Dear chef help me with the following {prompt}"
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
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
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
