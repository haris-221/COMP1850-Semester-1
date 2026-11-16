import random


# Get user to input how many random numbers they want

num_numbers = int(input("How many random numbers do you want to generate? "))
# Generate this many random numbers

random_numbers = [random.randint(1, 100) for _ in range(num_numbers)]

# Write the random numbers to a file named random.txt, one number per line
with open("names.txt", "w") as f:
    for num in random_numbers:
        f.write(f"{num}\n")
