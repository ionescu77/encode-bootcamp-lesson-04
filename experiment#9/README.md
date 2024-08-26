# README for Experiment
This README was generated from Issue #9

## To automate the following assignment in context of the @Codebase 

```
## Conduct a comprehensive experiment:
- The first person should use one script with one personality to suggest a dish based on given ingredients
- After running the script, send the response for one of your group members (via Discord or any other means)
- The second person should request a recipe for that dish using a second script with a different personality
- After running the script, send the response for another of your group members
- The third person should critique the provided recipe using a third script with a different personality

## Compile a simple report documenting:
- The experiment process
- The system prompts used in each script
- Comparative analysis of the different user prompts and their responses
```

To automate the assignment based on the given context, we can create a Python script that orchestrates the entire process. Here's a suggestion on how to approach this:

1. Create three separate Python scripts for each personality:
- chef_ingredient_suggester.py
- chef_recipe_provider.py
- chef_recipe_critic.py
2. Create a main script experiment_conductor.py that will orchestrate the entire process.
3. Use the existing OpenAI client setup and message structure from the provided codebase.

Here's an outline of the experiment_conductor.py script:

```python
import subprocess
import json
from openai import OpenAI

client = OpenAI()

def run_chef_script(script_name, input_data):
    result = subprocess.run(['python', script_name], input=input_data, text=True, capture_output=True)
    return result.stdout

def generate_report(ingredients, dish, recipe, critique):
    report = {
        "experiment_process": [
            "1. Suggested dish based on ingredients",
            "2. Generated recipe for the suggested dish",
            "3. Critiqued the generated recipe"
        ],
        "system_prompts": {
            "ingredient_suggester": "You are an experienced chef that suggests dishes based on given ingredients.",
            "recipe_provider": "You are a seasoned Italian chef with a passion for pasta-making.",
            "recipe_critic": "You are a young, enthusiastic Indian chef specializing in Biryani."
        },
        "user_prompts_and_responses": {
            "ingredient_suggester": {
                "input": f"Suggest a dish using these ingredients: {ingredients}",
                "output": dish
            },
            "recipe_provider": {
                "input": f"Provide a detailed recipe for {dish}",
                "output": recipe
            },
            "recipe_critic": {
                "input": f"Critique this recipe and suggest improvements: {recipe}",
                "output": critique
            }
        }
    }
    return json.dumps(report, indent=2)

# Main experiment flow
ingredients = input("Enter ingredients (comma-separated): ")

# Step 1: Suggest dish based on ingredients
suggested_dish = run_chef_script('chef_ingredient_suggester.py', ingredients)
print(f"Suggested dish: {suggested_dish}")

# Step 2: Generate recipe for the suggested dish
recipe = run_chef_script('chef_recipe_provider.py', suggested_dish)
print(f"Generated recipe: {recipe}")

# Step 3: Critique the generated recipe
critique = run_chef_script('chef_recipe_critic.py', recipe)
print(f"Recipe critique: {critique}")

# Generate and save the report
report = generate_report(ingredients, suggested_dish, recipe, critique)
with open('experiment_report.json', 'w') as f:
    f.write(report)

print("Experiment completed. Report saved as experiment_report.json")
```

For each of the chef scripts (`chef_ingredient_suggester.py`, `chef_recipe_provider.py`, `chef_recipe_critic.py`), you can use the structure from the existing `chef-gpt.py` file:

```python
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
          "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
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
```

Modify the system messages and user prompts in each script to match the specific personality and task.


To run the experiment:

1. Create the three chef scripts with their respective personalities and tasks.
2. Run the `experiment_conductor.py` script.
3. The script will automatically generate a JSON report with the experiment process, system prompts, and comparative analysis of the different user prompts and responses.


This approach automates the entire process, eliminating the need for manual intervention between steps and automatically generating a structured report of the experiment.
