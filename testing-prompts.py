from openai import OpenAI

client = OpenAI()

# Enter for user prompt and store it in messages
messages = [
    {
        "role": "user",
        "content": input("Type your prompt:\n"),
    }
]

# set model
model = "gpt-4o-mini"

# send request to OpenAI and stream the answer
stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
