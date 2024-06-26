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

def get_names(spicy_foods):
    rangez = len(spicy_foods)
    new_spicy_foods = list()
    for x in range(rangez):
        new_spicy_foods.append(spicy_foods[x].get("name"))
    return new_spicy_foods

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

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    spicy_foodz = len(spicy_foods)
    new_list = list()
    for i in range(spicy_foodz):
        if spicy_foods[i].get("cuisine") == cuisine:
            return spicy_foods[i]

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))
   

def get_average_heat_level(spicy_foods):
    length = len(spicy_foods)
    new_list = list()
    for x in range(length):
        new_list.append(spicy_foods[x].get("heat_level"))
    return sum(new_list) / length

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
