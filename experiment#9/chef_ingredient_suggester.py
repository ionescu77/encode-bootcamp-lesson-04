from openai import OpenAI
import os
import sys

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def suggest_dish(ingredients):
   messages = [
       {
           "role": "system",
           "content": "You are an experienced chef that suggests dishes based on given ingredients. You have a passion for creating delicious meals with whatever ingredients are available. Your suggestions should be creative yet practical, focusing on dishes that can be made primarily with the provided ingredients."
       },
       {
           "role": "user",
           "content": f"Suggest a dish using these ingredients: {ingredients}"
       }
   ]

   response = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=messages,
       max_tokens=100
   )

   return response.choices[0].message.content.strip()

def main():
   print("Welcome to the Chef's Ingredient-Based Dish Suggester!")
   print("Type 'quit' at any time to return to the main script.")
   ingredients = sys.stdin.read().strip()
   while True:

       if not ingredients:
           print("Please enter ingredients.")
           ingredients = input("\nWhat ingredients do you have? (Separate with commas) ")
           continue

       if ingredients.lower() == 'quit':
           print("Thank you for using our service. Bon appétit!")
           break

       try:
           suggestion = suggest_dish(ingredients)
           print(suggestion)
       except Exception as e:
           print(f"Oops! Something went wrong: {str(e)}")

       continue_choice = input("\nWould you like another suggestion? (yes/no): ")
       if continue_choice.lower() != 'yes':
           print("Thank you for using our service. Happy cooking!")
           break

if __name__ == "__main__":
   main()