from flask import Flask, render_template

app = Flask(__name__)

recipes = [
    {
    "id": 1,
    "name": "Chicken Biryani",
    "description": "Authentic Hyderabadi style Chicken Biryani with proper marination.",
    "image": "Biryani.jpg",
    "prep_time": "20 minutes",
    "cook_time": "40 minutes",
    "servings": "4 people",
    "ingredients": """
For Marination:
500 grams Chicken, 1/2 cup Thick Curd (Yogurt), 
2 tablespoons Ginger-Garlic paste, 1 teaspoon Turmeric Powder, 
2 teaspoons Red Chilli Powder, 1 tablespoon Garam Masala, 
1 teaspoon Coriander Powder, 1 teaspoon Cumin Powder, 
Salt to taste, 2 tablespoons Lemon Juice.

For Rice:
2 cups Basmati Rice, 4 Cloves, 2 Cardamom, 
1 Bay Leaf, 1 small Cinnamon stick, Salt to taste.

Other Ingredients:
2 large Onions (thin sliced), 4 tablespoons Oil, 
2 tablespoons Ghee, Fresh Mint Leaves, Fresh Coriander Leaves.
""",
"steps": """
Step 1: Wash and clean chicken pieces properly.

Step 2: In a large bowl, mix chicken with curd, ginger-garlic paste,
turmeric, chilli powder, garam masala, coriander powder,
cumin powder, salt and lemon juice.

Step 3: Cover and marinate for minimum 1 hour
(best if refrigerated for 2–4 hours).

Step 4: Wash basmati rice and soak for 30 minutes.

Step 5: Boil water with whole spices and salt.
Cook rice 70% and drain.

Step 6: Heat oil and ghee in a heavy pan.
Fry sliced onions until golden brown.

Step 7: Add marinated chicken and cook for 10–12 minutes.

Step 8: Layer partially cooked rice over chicken.

Step 9: Add fried onions, mint and coriander.

Step 10: Cover tightly and cook on low flame (dum)
for 15–20 minutes.

Step 11: Rest for 5 minutes, mix gently and serve hot.
"""
    },
    {
        "id": 2,
        "name": "Paneer Butter Masala",
        "description": "Creamy paneer curry.",
        "image": "Paneer-Butter-Masala.jpg",
        "ingredients": "Paneer, Tomato puree, Butter, Cream, Spices",
        "steps": "1. Cook tomato gravy.\n2. Add spices.\n3. Add paneer cubes.\n4. Simmer and add cream."
    },
    {"id": 3, "name": "Veg Fried Rice", "description": "Fried rice with vegetables", "image": "Veg-Fried-Rice.jpg"},
    {"id": 4, "name": "Masala Dosa", "description": "Crispy dosa with potato filling", "image": "Masala-Dosa.jpg"},
    {"id": 5, "name": "Chole Bhature", "description": "Chickpea curry with fried bread", "image": "Chole-Bhature.jpg"},
    {"id": 6, "name": "Gulab Jamun", "description": "Sweet dessert in sugar syrup", "image": "Gulab-Jamun.jpg"},
]

@app.route("/")
def home():
    return render_template("home.html", recipes=recipes)
@app.route("/recipe/<int:id>")
def recipe_detail(id):
    recipe = next((r for r in recipes if r["id"] == id), None)
    if recipe is None:
        return "Recipe not found", 404
    return render_template("recipe.html", recipe=recipe)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
