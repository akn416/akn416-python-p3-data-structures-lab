spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_spiciest_foods(spicy_foods):
    rangez = len(spicy_foods)
    newlist = list()
    for x in range(rangez):
        if spicy_foods[x].get("heat_level") > 5:
            newlist.append(spicy_foods[x])
    return newlist

def print_spicy_foods(spicy_foods):
    for each_food in spicy_foods:
        print(f'{each_food["name"]} ({each_food["cuisine"]}) | Heat Level: {each_food["heat_level"] * "🌶 "}')

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

print_spiciest_foods(spicy_foods)