from openai import OpenAI
import os
import sys

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def critique_recipe(recipe):
    messages = [
        {
            "role": "system",
            "content": "You are a young, enthusiastic Indian chef specializing in Biryani. You have a keen eye for culinary techniques and a passion for fusion cuisine. Your critiques are constructive, focusing on potential improvements and creative twists while respecting the original recipe."
        },
        {
            "role": "user",
            "content": f"Critique this recipe and suggest improvements: {recipe}"
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500
    )

    return response.choices[0].message.content

def main():
    print("Welcome to the Recipe Critic!")
    print("Please provide a recipe for critique.")
    recipe = sys.stdin.read().strip()

    if not recipe:
        print("No recipe provided. Exiting.")
        return

    try:
        critique = critique_recipe(recipe)
        print("\nHere's the critique and suggestions:")
        print(critique)
    except Exception as e:
        print(f"Oops! Something went wrong: {str(e)}")

if __name__ == "__main__":
    main()