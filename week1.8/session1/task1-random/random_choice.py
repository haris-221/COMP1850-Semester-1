import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
num_names = int(input("How many names do you want to choose? "))
chosen_names = random.sample(names, num_names)

# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
for name in chosen_names:
    print(name)
