import sys, random

print("Welcome to the Silly Name Generator!\n")
print("This program will generate a random silly name for you")

first_names = ("Portabella", "Fifa", "Maybelline", "Phelony", "Spicy", "Birdella", "Candida",
            "Slayer", "Buddy Bear", "Christop", "Chip", "Everest", "Omega")
last_names = ("Bacon", "Beefman", "Onions", "Sweetman", "Peacock", "Baldhead",
            "Giggle", "Jumble", "Bottoms")

while True:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    print("\n")
    print(f"> {first_name} {last_name}", file=sys.stderr)
    print("\n")

    try_again = input("Press ENTER to generate a new silly name or enter N to exit the generator ")
    if try_again.lower() == "n":
        break
    else:
        continue
