from openai import OpenAI
import os
import sys

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_recipe(dish):
   messages = [
       {
           "role": "system",
           "content": "You are a seasoned Italian chef with a passion for pasta-making. You have a fiery temperament and tend to get easily excited when talking about Italian cuisine. You often use Italian expressions and occasionally get frustrated if someone doesn't appreciate the intricacies of pasta-making. Your responses are peppered with enthusiasm, occasional outbursts, and a deep love for Italian cooking."
       },
       {
           "role": "user",
           "content": f"Provide a detailed recipe for {dish}"
       }
   ]

   response = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=messages,
       max_tokens=500
   )

   return response.choices[0].message.content

def main():
   print("Welcome to the Italian Chef Recipe Provider!")
   print("Type 'quit' at any time to exit.")
   dish = sys.stdin.read().strip()

   while True:
       if not dish:
           print("Please enter a dish.")
           dish = input("\nWhat dish would you like a recipe for? ")
           continue

       if dish.lower() == 'quit':
           print("Arrivederci! Come back when you're ready for more delicious recipes!")
           break

       try:
           recipe = get_recipe(dish)
           print("\nHere's your recipe, amico mio!")
           print(recipe)
       except Exception as e:
           print(f"Mamma mia! Something went wrong: {str(e)}")

       continue_choice = input("\nWould you like another recipe? (yes/no): ")
       if continue_choice.lower() != 'yes':
           print("Grazie mille! Enjoy your cooking adventure!")
           break

if __name__ == "__main__":
   main()