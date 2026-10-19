import random
print("Welcome to dice roller! ")
num = int(input("How many dice do you want to roll? "))
def roll_dice():
    return random.randint(1,6)
for i in range(num):
    print(f"Dice {i+1}: {roll_dice()}")