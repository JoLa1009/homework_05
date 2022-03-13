# homework 5.6 Geography Quiz

import random

capitals = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Italy": "Rome", "France": "Paris",
            "Germany": "Berlin", "Switzerland": "Bern", "Netherlands": "Amsterdam", "Greece": "Athen", "Serbia": "Belgrade",
            "Slovakia": "Bratislava", "Belgium": "Brussels", "Romania": "Bucharest","Hungary": "Budapest",
            "Denmark": "Copenhagen", "Ireland": "Dublin", "Finland": "Helsinki", "Ukraine": "Kiev", "Portugal": "Lisbon",
            "Slovenia": "Ljunbljana", "United Kingdom": "London", "Luxembourg": "Luxembourg", "Norway": "Oslo",
            "Czech Republic": "Prague", "Island": "Reykjavik", "Sweden": "Stockholm"}
list_countries = []
num = 0

for country_capital in capitals.keys():
    list_countries.append(country_capital)

list_rand =[]

for i in range(5):
    rand = random.randint(0, 25)

    while rand in list_rand:
        rand = random.randint(0,25)

    country = list_countries[rand]
    input_user = input("What's the capital of " + str(country) + "? ")
    capital = capitals[str(country)]

    if input_user == capital:
        print("That's correct!")
        num += 1
    else:
        print("That's wrong! The capital of " + str(country) + " is " + str(capital) + "!")
    list_rand.append(rand)

print(str(num) + " capitals were correctly assigned. Well done!")





