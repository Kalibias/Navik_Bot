import json
import random
import requests
import textwrap
import re

# Setting up the variables for future uses.
card_facing = ["Reversed", "Upright"]
tarot_arcana = ["Major", "Minor"]

# Assigning Suits to their number to make Iteration easier.
suit_dict = {
    "Ace": 0,
    "Two": 1,
    "Three": 2,
    "Four": 3,
    "Five": 4,
    "Six": 5,
    "Seven": 6,
    "Eight": 7,
    "Nine": 8,
    "Ten": 9,
    "Page": 10,
    "Knight": 11,
    "Queen": 12,
    "King": 13
}
min_dict = {
    "Pentacles": 0,
    "Cups": 1,
    "Swords": 2,
    "Wands": 3
}
maj_dict = {
    "Fool": 0,
    "Magician": 1,
    "High Priestess": 2,
    "Empress": 3,
    "Emperor": 4,
    "Hierophant": 5,
    "Lovers": 6,
    "Chariot": 7,
    "Strength": 8,
    "Hermit": 9,
    "Wheel of Fortune": 10,
    "Justice": 11,
    "Hanged Man": 12,
    "Death": 13

}

bad_beans = ["Barf",
             "Toothpaste",
             "Booger",
             "Rotten Egg",
             "Baby Wipes",
             "Black Pepper",
             "Skunk Spray",
             "Moldy Cheese",
             "Motor Oil",
             "Dried Blood",
             "Ear Wax",
             "Pencil Shavings",
             "Canned Dog Food",
             "Centipede",
             "Stinky Socks",
             "Lawn Clippings",
             "Spoiled Milk",
             "Dead Fish",
             "Stink Bug",
             "Dirty Dishwater",
             "Old Bandage",
             "Liver & Onion",
             "Evil Coconut",
             "Benry"
             ]

good_beans = ["Water Gate Salad", "Cream Cheese", "Lemon", "Peach", "Berry Blue", "Juicy Pear", "Buttered Popcorn",
              "Coconut", "Plum", "Licorice",
              "Caramel Corn", "Lime", "Cafe Latte", "Chocolate Pudding", "Strawberry Jam",
              "Tutti-Frutti", "Strawberry Banana Smoothie", "Toasted Marshmallow", "Birthday Cake", "Pomegranate",
              "Cappuccino"]


def tarot_draw():
    with open("DBs/Arcana.json", encoding="UTF-8") as tarot:
        tarot = json.load(tarot)
    arcana = random.choice(tarot_arcana)
    facing = random.choice(card_facing)
    meaning = 'key_means' if facing == "Upright" else 'rev_means'

    if arcana == "Major":
        maj_arc = random.choice(list(maj_dict.keys()))
        drawn_card = f"You card is {maj_arc} \n{facing}"
        result = tarot["Major"][int(maj_dict[maj_arc])][maj_arc][0][meaning]
        card = "\n".join(textwrap.wrap(result, 90))

    elif arcana == "Minor":
        min_arc = random.choice(list(min_dict.keys()))
        suit = random.choice(list(suit_dict.keys()))
        drawn_card = f"You card is {suit} of {min_arc} \n{facing}"
        result = tarot["Minor"][min_arc][suit_dict[suit]][suit][0][meaning]
        card = "\n".join(textwrap.wrap(result, 90))
    print(f"{drawn_card}\n{card}")
    return f"{drawn_card}\n{card}"


def send_joke():
    joke_data = r"https://official-joke-api.appspot.com/random_joke"
    data = requests.get(joke_data)
    joke = json.loads(data.text)

    print(f"{joke['setup']} \n{joke['punchline']}")
    return f"{joke['setup']} \n{joke['punchline']}"


def bean_roulette():
    bean_pick = ["Bad", "Good"]
    with open("DBs/beanlist.json", encoding="UTF-8") as bean_list:
        bean_list = json.load(bean_list)
    bean_pick = random.choice(list(bean_pick))

    if bean_pick == "Bad":
        picked_bean = random.choice(list(bad_beans))
        bean_descript = bean_list["Bad"][0][picked_bean].lower()
        return f"The unforunate bean picked: {picked_bean}. \nDescription: {bean_descript}."
    else:
        picked_bean = random.choice(list(good_beans))
        bean_descript = bean_list["Good"][0][picked_bean].lower()
        return f"The lucky bean picked: {picked_bean}. \nDescription: {bean_descript}"


def dice_roll(ans):
    ans_split = re.search(r"(\d+)d(\d+)", ans)
    print(ans_split.groups())
    dice = int(ans_split.group(1))
    sides = int(ans_split.group(2))
    amount = 0

    while dice > 0:
        amount += random.randint(1, sides)
        print(amount)
        dice -= 1

    print(f"final answer: {amount}")
    return amount



#
