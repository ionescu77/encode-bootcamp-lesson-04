import subprocess
import json
from openai import OpenAI
from datetime import datetime

client = OpenAI()

def run_chef_script(script_name, input_data):
    result = subprocess.run(['python', script_name], input=input_data, text=True, capture_output=True)
    return result.stdout

def generate_report(ingredients, dish, recipe, critique):
    report = {
        "timestamp": datetime.now().isoformat(),
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