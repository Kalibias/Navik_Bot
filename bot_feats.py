import json
import random
import requests
import textwrap
import re

# Setting up the variables for future uses.

# Assigning Suits to their number to make Iteration easier.


def tarot_draw():
    arcana = random.choice(("Major", "Minor"))
    facing = random.choice(("Upright", "Reversed"))
    meaning = 'key_means' if facing == "Upright" else 'rev_means'

    with open("DBs/Arcana.json", encoding="UTF-8") as tarot:
        tarot = json.load(tarot)

    if arcana == "Major":

        maj_arc = random.choice(list(tarot["Major"].keys()))
        drawn_card = f"You card is {maj_arc} \n{facing}"
        result = tarot["Major"][maj_arc][meaning]
        card = "\n".join(textwrap.wrap(result, 90))

    elif arcana == "Minor":
        # Draws the card and its suit.
        min_arc = random.choice(list(tarot["Minor"].keys()))
        suit = random.choice(list(tarot["Minor"][min_arc].keys()))

        # Complies the card's suit title and description
        card = f"You card is {suit} of {min_arc} \n{facing}"
        description = tarot["Minor"][min_arc][suit][meaning]
        description = "\n".join(textwrap.wrap(description, 90))

    print(f"{card}\n{description}\n")
    return f"{card}\n{description}\n"


# This draws multiple cards
def tarot_roll(number):
    result = ""
    for i in range(number):
        result += tarot_draw()
    return result



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
        picked_bean = random.choice(list(bean_list["Bad"].keys()))
        bean_descript = bean_list["Bad"][picked_bean].lower()
        return f"The unfortunate bean picked: {picked_bean}. \nDescription: {bean_descript}."
    else:
        picked_bean = random.choice(list(bean_list["Good"].keys()))
        bean_descript = bean_list["Good"][picked_bean].lower()
        return f"The lucky bean picked: {picked_bean}. \nDescription: {bean_descript}"

def dice_roll(ans):

    ans_split = re.search(r"(\d+)d(\d+)", ans)
    if ans_split is None:
        return random.randint(1, int(ans))
    dice = int(ans_split.group(1))
    sides = int(ans_split.group(2))
    amount = 0

    while dice > 0:
        amount += random.randint(1, sides)
        print(amount)
        dice -= 1

    print(f"final answer: {amount}")
    return amount



