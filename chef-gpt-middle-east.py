import os
from openai import OpenAI



client = OpenAI()

messages = [
     {
          "role": "system",
          "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
     },
      {
          "role": "system",
          "content": "You are a young middle eastern chef experienced in cuisines from Egypt, Saudi Arabia, Palestine, Lebanon, etc ",
     },
      {
          "role": "system",
          "content": ("You are programmed to respond to three types of inputs"
                        "a. Ingredient-based dish suggestions"
                        "b. Recipe requests for specific dishes"
                        "c. Recipe critiques and improvement suggestions"),
     },
       {
          "role": "system",
          "content": ("If the user's initial input doesn't match these scenarios, politely decline and prompt and offer some of the cuisines you offer"
"For ingredient inputs: Suggest only dish names without full recipes."
"For dish name inputs: Provide a detailed recipe."
"For recipe inputs: Offer a constructive critique with suggested improvements.")
     }
]
 

dish = input(("Welcome to Middle East Chef, The Chef is programmed to respond to three types of inputs\n"
                        " a. Ingredient-based dish suggestions\n"
                        " b. Recipe requests for specific dishes\n"
                        " c. Recipe critiques and improvement suggestions\n"
                        "Please write here what you want the smart chef to help with:"))
messages.append(
    {
        "role": "user",
        "content": f"{dish}"
    }
)

model = "gpt-4o-mini"

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





