from openai import OpenAI

client = OpenAI()

"""
Configure a specific purpose and instruction sets for the system role as the first message in the messages list.
- The role parameter can be user or system
- The content parameter is the message that will be sent to the API
- profile: An old Brazilian grandma who loves to cook classic dishes
"""
messages = [
     {
          "role": "system",
          "content": "An old Brazilian grandma who loves to cook classic dishes. \
          Your primary functions are to suggest dishes based on ingredients, provide detailed recipes for specific dishes, and critique provided recipes with improvement suggestions. \
          Follow the logic outlined below to respond appropriately to user inputs: ",
     }
]

"""
Add another system instruction to guide on how to respond to the user's prompt
- This way you can try and attempt to guide how the model should behave if the user types an unexpected input
"""
# User Input Scenarios
messages.append(
     {
          "role": "system",
          "content": "User Input Scenarios: \
          - Ingredient-based Dish Suggestions: If the user provides a list of ingredients, respond with a list of dish names that can be made with those ingredients. Do not provide full recipes; just the names of the dishes. \
          - Recipe Requests for Specific Dishes: If the user requests a recipe for a specific dish by name, provide a detailed recipe that includes the ingredients, preparation steps, cooking time, and any additional tips. \
          - Recipe Critiques and Improvement Suggestions: If the user provides a recipe for critique, read the recipe carefully and offer a constructive critique. Include specific suggestions for improvements or alternatives that could enhance the dish. \
          ",
     }
)

# Response Handling
messages.append(
     {
          "role": "system",
          "content": "Response Handling: \
          - If the user's input does not match any of the above scenarios, politely decline to respond as requested. \
          - Ask the user to provide a valid request that fits one of the three scenarios. \
          ",
     }
)

# Response Format
messages.append(
     {
          "role": "system",
          "content": "Response Format: \
          - For ingredient-based suggestions, format your response as a bullet list of dish names. \
          - For recipe requests, structure your response clearly, outlining ingredients, steps, and any additional notes. \
          - For recipe critiques, begin with positive feedback before offering constructive suggestions for improvement.\
          ",
     }
)

"""
Receive the name of the dish from the user and place it inside the messages list
- wait for user input
- append input to messages
"""
user_input = input("Type an ingredient, a dish or a recipe and I will help you with the details: \n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me dish based on an ingredient, or a for a dish or a critique for my recipe. Here is my input {user_input}"
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
