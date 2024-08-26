# encode-bootcamp-lesson-04

## About
This repo contains code, related to the Weekend 1 Exercises.
You can find test scripts and also scripts used for the experiment.

```bash
.
├── README.md                        # this README
├── chef-gpt-extended-3choices.py    # draft
├── chef-gpt-indian.py               # experiment @ionescu77 
├── chef-gpt-italian.py              # experiment @ionescu77
├── chef-gpt-original.py             # experiment @ionescu77
├── chef-gpt.py                      # draft
├── experiment#9                     # folder experiment @alexmazaltov see Issue #9
├── pyrightconfig.json               # editor settings
├── test_openai-api.py               # test script
├── testing-prompts.py               # test script
└── venv
```
## Contributors
@alexmazaltov, @ionescu77

## How to use
Please note the following how-to is specific to MacOS & Linux systems.

To use the code:
- clone this repository; into an empty folder run:
```bash
git clone git@github.com:ionescu77/encode-bootcamp-lesson-04.git
```
- create a python `venv` (virtual environment)
```bash
python3 -m venv venv
```
- install the requirements
```bash
pip install openai
```
- activate de `venv`
```bash
source venv/bin/activate
```
- make sure to export an ENV variable for API key (environment variable)
```bash
export OPENAI_API_KEY="--your-openai-api-key--here--"
echo $OPENAI_API_KEY
```
- repo contains a `.gitignore` for the `venv` so you might [set the ENV variables in the virtual environment](https://stackoverflow.com/a/38645983/2861978)
- run the code, for example:
```bash
python test_openai-api.py
```

  
## Weekend Project

To consolidate the knowledge acquired this week, students should complete the following project:

- [x] 1. Create a new GitHub repository for your project.
- [x] 2. Invite all members of your group to collaborate on the repository. (invited known github ID handles)
- [x] 3. Write a simple README.md file explaining your project (ongoing)
- [x] 4. Modify and expand the `Chef GPT script` by incorporating a unique personality for your AI chef
- [x] 4.1.  - Tweak the system prompt to include a unique personality for your AI chef
   - Example personalities:
     - A young, enthusiastic Indian chef specializing in Biryani
     - A seasoned Italian chef with a passion for pasta-making
     - An old Brazilian grandma who loves to cook classic dishes
- [ ] 5. Develop individual scripts for each group member, each featuring a distinct AI chef personality
- [x] 6. Program the AI to respond to three specific types of user inputs:
   - a. Ingredient-based dish suggestions
   - b. Recipe requests for specific dishes
   - c. Recipe critiques and improvement suggestions
- [x] 7. Give enough instructions in the system prompt to make the AI conform to give the responses according to the scenarios above
   - Implement the following logic:
   - If the user's initial input doesn't match these scenarios, politely decline and prompt for a valid request.
     - For ingredient inputs: Suggest only dish names without full recipes.
     - For dish name inputs: Provide a detailed recipe.
     - For recipe inputs: Offer a constructive critique with suggested improvements.
   - Ideally, the same AI would be able to handle the three scenarios above
     - But if you can't get the same AI to do that, you can make three different scripts for each personality to proceed with your project
- [ ] 8. Conduct a comprehensive experiment:
   - The first person should use one script with one personality to suggest a dish based on given ingredients
     - After running the script, send the response for one of your group members (via Discord or any other means)
   - The second person should request a recipe for that dish using a second script with a different personality
     - After running the script, send the response for another of your group members
   - The third person should critique the provided recipe using a third script with a different personality
- [ ] 9. Compile a simple report documenting:
   - The experiment process
   - The system prompts used in each script
   - Comparative analysis of the different user prompts and their responses
- [ ] 10. Submit your completed project through the designated submission form.

> You should find your group in the [Discord](https://discord.gg/encodeclub) AI Bootcamp Channel
>
> > If you can't find your group, please contact the program manager through Discord or email

## Report

### Experiment process
   - The first person should use one script with one personality to suggest a dish based on given ingredients
     - After running the script, send the response for one of your group members (via Discord or any other means)
   - The second person should request a recipe for that dish using a second script with a different personality
     - After running the script, send the response for another of your group members
   - The third person should critique the provided recipe using a third script with a different personality

### System Prompts
1. First Person (indian chef profile):
```bash
python chef-gpt-indian.py
Type an ingredient, a dish or a recipe and I will help you with the details:
onions, curry, chicken
Based on the ingredients you provided (onions, curry, chicken), here are some dish suggestions:

- Chicken Curry
- Chicken Biryani
- Chicken Korma
- Chicken Masala
- Chicken Vindaloo
- Onion Chicken Stir-fry

Feel free to ask for a recipe for any specific dish or provide a recipe for critique!
```
2. Second Person (italian chef profile):
```bash
python chef-gpt-italian.py
Type an ingredient, a dish or a recipe and I will help you with the details:
Chicken Vindaloo
It seems like your request does not fit neatly into one of the three scenarios. Please provide either a list of ingredients for dish suggestions, a specific dish for which you would like a recipe, or a recipe you would like me to critique.

Chicken Korma
I can provide you with a detailed recipe for Chicken Korma. Here it is:

### Chicken Korma Recipe

#### Ingredients:
- 1 kg chicken, bone-in, skinless, cut into pieces
- 2 large onions, finely sliced
- 4 tablespoons cooking oil or ghee
- 2 teaspoons ginger-garlic paste
- 1 cup plain yogurt
- 1/2 cup cream (optional for richness)
- 1/4 cup ground almonds or cashews
- 2-3 green chilies, slit (adjust for spice preference)
- 1/2 teaspoon turmeric powder
- 1-2 teaspoons red chili powder (adjust for spice preference)
- 1 teaspoon garam masala
- 1 teaspoon cumin powder
- 1 teaspoon coriander powder
- Salt, to taste
- Fresh cilantro, chopped (for garnish)
- Whole spices (2-3 green cardamoms, 2-3 cloves, 1-inch cinnamon stick, and 2 bay leaves)

#### Preparation Steps:
1. **Marinate the Chicken**: In a bowl, mix the chicken pieces with yogurt, ginger-garlic paste, turmeric powder, red chili powder, cumin powder, coriander powder, and salt. Cover and marinate for at least 1 hour, preferably overnight in the refrigerator for better flavor.

2. **Cook the Onions**: In a large pot or deep pan, heat the oil or ghee over medium heat. Add the sliced onions and cook until they turn golden brown.

3. **Add Whole Spices**: Once the onions are browned, add the whole spices (cardamom, cloves, cinnamon, and bay leaves) and sauté for a minute until fragrant.

4. **Combine Chicken**: Add the marinated chicken to the pot. Cook on medium heat for 5-7 minutes, stirring occasionally until the chicken is browned on all sides.

5. **Add Liquid**: Stir in the cream and ground almonds/cashews. If needed, add water to ensure the chicken is mostly submerged. Bring to a boil, then reduce heat to low.

6. **Simmer**: Cover the pot and let it simmer for about 30-40 minutes, stirring occasionally, until the chicken is cooked through and tender.

7. **Finish with Garam Masala**: In the last few minutes of cooking, add the garam masala and slit green chilies. Stir well and adjust seasoning if necessary.

8. **Serve**: Garnish with chopped cilantro before serving.

### Additional Tips:
- Serve with naan, roti, or steamed rice to soak up the delicious gravy.
- Adjust the amount of cream and nuts based on preferred richness and consistency.
- For extra flavor, consider adding a tablespoon of lemon juice just before serving.

Enjoy your Chicken Korma! Let me know if you need any further assistance!

```
3. Third Person (brazilian chef profile)
```bash
python chef-gpt-brazilian.py
Type an ingredient, a dish or a recipe and I will help you with the details:
### Chicken Korma Recipe

#### Ingredients:
- 1 kg chicken, bone-in, skinless, cut into pieces
- 2 large onions, finely sliced
- 4 tablespoons cooking oil or ghee
- 2 teaspoons ginger-garlic paste
- 1 cup plain yogurt
- 1/2 cup cream (optional for richness)
- 1/4 cup ground almonds or cashews
- 2-3 green chilies, slit (adjust for spice preference)
- 1/2 teaspoon turmeric powder
- 1-2 teaspoons red chili powder (adjust for spice preference)
- 1 teaspoon garam masala
- 1 teaspoon cumin powder
- 1 teaspoon coriander powder
- Salt, to taste
- Fresh cilantro, chopped (for garnish)
- Whole spices (2-3 green cardamoms, 2-3 cloves, 1-inch cinnamon stick, and 2 bay leaves)

# ... removed lines ...

If you would like a detailed recipe for any specific dish or have more ingredients to share, just let me know!

 5-7 minutes, stirring occasionWith chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, and turmeric powder, you can create these delicious dishes:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Chicken with Cashew Nut Sauce

If you would like a detailed recipe for any of these dishes or if you have more ingredients to share, just let me know!

ally until the chicken is browned on all sides.

5. **Add LiquiWith chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, and red chili powder, you can prepare these flavorful dishes:

- Spicy Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Cashew Chicken with Spices

If you'd like a detailed recipe for any specific dish or have more ingredients to share, feel free to ask!

d**: Stir in the cream andWith chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, red chili powder, and garam masala, here are some delicious dishes you can make:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Mughlai Chicken

If you would like a detailed recipe for any specific dish or if there are more ingredients you'd like to share, just let me know!

 ground almonds/cashews. IWith chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, red chili powder, garam masala, and cumin powder, you can create these rich and aromatic dishes:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Mughlai Chicken with Cumin

If you’d like a detailed recipe for any specific dish or have more ingredients to share, feel free to ask!

f needed, add water to ensure With chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, red chili powder, garam masala, cumin powder, and coriander powder, here are some delightful dishes you can prepare:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Mughlai Chicken

If you would like a detailed recipe for any specific dish or if you have more ingredients to share, just let me know!

the chicken is moWith chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, red chili powder, garam masala, cumin powder, coriander powder, and salt, you can create these delicious dishes:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Mughlai Chicken

If you'd like a detailed recipe for any of these dishes or if you have more ingredients to share, just let me know!

stly submerged. Bring to a boil, then reWith all your ingredients, including chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, red chili powder, garam masala, cumin powder, coriander powder, salt, and fresh cilantro for garnish, you can make:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Mughlai Chicken

If you'd like, I can provide a detailed recipe for any of these dishes! Just let me know which one you're interested in!

duce heat to low.

6. **Simmer**: Cover the pot and let it simmer for about 30-40 minutes,With all your ingredients, including chicken, onions, cooking oil or ghee, ginger-garlic paste, plain yogurt, cream, ground almonds or cashews, green chilies, turmeric powder, red chili powder, garam masala, cumin powder, coriander powder, salt, fresh cilantro for garnish, and the whole spices (green cardamoms, cloves, cinnamon stick, and bay leaves), you can prepare these aromatic and flavorful dishes:

- Chicken Korma
- Butter Chicken
- Chicken Tikka Masala
- Spicy Chicken Curry
- Mughlai Chicken

If you’d like a detailed recipe for any specific dish or need assistance with something else, just let me know!

 It seems there was no input. If you have a specific request—whether it's for a recipe, dish suggestions from ingredients, or a recipe critique—please let me know! I’m here to help.

stirring occasionally, uIt looks like you haven't provided the preparation steps for a specific recipe or a complete request related to a dish. If you have a specific recipe you’d like me to critique, or if you need detailed preparation steps for a particular dish using the ingredients you've listed, please let me know! I'm happy to assist you!

ntil the chicken is cooked through and tender.

7. **Finish with Garam Masala**: In the last few minutes of cooking, add the garam masala and slit green chilies. Stir well and adjust seasoning if necessary.

8. **Serve**: Garnish with chopped cilantro before serving.

### AThis is a great start to your Chicken dish! Here’s some positive feedback, followed by suggestions for improvement:

### Positive Feedback:
- **Marination**: Marinating the chicken with yogurt and spices will tenderize the meat and infuse it with flavor, enhancing the dish significantly.
- **Use of Spices**: The combination of spices you're using is traditional and should provide a lovely depth of flavor.

### Suggestions for Improvement:
1. **Add Acid**: Consider adding a splash of lemon juice or vinegar to the marinade. This will not only help to tenderize the chicken even more but will also add a nice tang that balances the richness of the yogurt.

2. **Spice Balance**: If you want to deepen the flavor profile, you can add some whole spices (like a couple of cardamom pods or cloves) during the marination process.

3. **Time**: While marinating for at least 1 hour is good, overnight is quite ideal as it allows the spices to penetrate deeply.

4. **Temperature**: Make sure the chicken reaches room temperature before cooking for more even cooking. You can take it out of the fridge about 30 minutes before you start cooking.

5. **Incorporate Fresh Herbs**: If possible, consider adding some chopped fresh cilantro or mint into the marinade for an extra layer of flavor.

If you have more preparation steps to share or need further assistance, feel free to let me know!

dIt looks like there was no input in your last message. If you have additional preparation steps you'd like to share, or if you have any questions or need assistance with a specific recipe or dish, just let me know! I'm here to help!

ditional Tips:
- Serve with naan, roti, or steamed rice to soak up the delicious gravy.
- Adjust the amount of cream and nuts based on preferred richnesYour second preparation step for cooking the onions is very good! Here's some positive feedback along with suggestions for improvement:

### Positive Feedback:
- **Cooking Onions**: Cooking onions until golden brown is essential as it builds a rich base for the dish, enhancing the overall flavor.
- **Oil or Ghee**: Using ghee will add a wonderful richness and aroma to the dish, which complements the spices beautifully.

### Suggestions for Improvement:
1. **Timing and Patience**: Make sure to cook the onions slowly over medium heat to develop their sweetness without burning them. This can take about 10-15 minutes.

2. **Add a Pinch of Salt**: This will help draw out the moisture from the onions and allow them to cook down faster and more evenly.

3. **Deglazing**: After browning the onions, consider adding a splash of water or stock to deglaze the pan. This will loosen the brown bits stuck to the bottom, which will add more flavor to your dish.

4. **Layering Flavors**: Once the onions are golden brown, you could also add the whole spices (like cardamom, cloves, and cinnamon) at this stage to enhance the aroma and flavor profile before moving on to the next steps.

If you have more preparation steps to share or need further assistance, feel free to let me know!

sIt looks like there wasn't any input in your last message. If you have additional preparation steps to provide, questions to ask, or if you need help with a recipe or dish suggestions, please let me know! I'm here to assist you!

 and consistency.
- For extra flavor, consider adding a tablespoon of lemon juice just before serving.

Enjoy your Chicken Korma! Let me know if you need any fuThis step of adding the whole spices after browning the onions is excellent! Here’s some positive feedback along with suggestions for improvement:

### Positive Feedback:
- **Layering Flavor**: Adding whole spices to the oil showcases traditional cooking methods that enhance the flavor profile of your dish, creating an aromatic base.
- **Timing**: Sautéing the spices until fragrant helps to release their essential oils, which will make your dish more flavorful.

### Suggestions for Improvement:
1. **Watch the Heat**: Be careful not to overheat the oil after adding the spices, as they can burn quickly and turn bitter. A low to medium heat is ideal during this step.

2. **Adjusting Quantity**: If you enjoy bold flavors, consider slightly increasing the number of whole spices, but make sure they complement rather than overpower the other flavors.

3. **Order of Addition**: If you happen to be using it, adding a bit of dried red chili at this stage can infuse a nice heat into the oil, giving your dish a more complex flavor right from the start.

4. **Stirring Constantly**: Stir the spices constantly for about 30 seconds to a minute to ensure even cooking and optimal extraction of flavors without browning them too much.

If you have more preparation steps to share or would like further assistance, please feel free to continue!

rIt seems your last message didn't come through. If you have any additional preparation steps you'd like to share, questions, or need further help with your recipe, please let me know! I'm here to assist you!

^Cobject address  : 0x1049b3e20
object refcount : 3
object type     : 0x10308e4d8
object type name: KeyboardInterrupt
object repr     : KeyboardInterrupt()
lost sys.stderr
```
### Comparative analysis

Conclusions after this experiment:
- it is hard as a human to write an AI `system` instruction set
- I had to use AI ChatGPT to help me create instructions for my experiment
- The first two steps with less user input (ingredients, dish name) very easy to handle
- The third step where I had to input a whole recipe was chalening
- For recipe the user input is too long, one has to process the input and remove `\n` NEWLINE
- Due to NEWLINE there was difficult to extract the feedback, I had to interrupt the 3rd person script
