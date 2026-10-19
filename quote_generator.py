import random
quotes = [
    "Believe in yourself and all that you are.",
    "Great things take time.",
    "Never stop learning because life never stops teaching.",
    "Success begins with small efforts.",
    "Dream big and work hard.",
    "Every day is a new opportunity.",
    "Do something today that your future self will thank you for.",
    "Mistakes are proof that you are trying.",
    "Discipline is the key to success.",
    "Your only limit is your mind.",
    "Don't be afraid to start again.",
    "Little progress every day adds up to big results.",
    "Hard work beats talent when talent doesn't work hard.",
    "Be stronger than your excuses.",
    "The secret of getting ahead is getting started."
]

print("    RANDOM QUOTE GENERATOR      ")
while True:
    print("\n1. Generate a quote")
    print("2. Exit")
    choice =input("Enter your choice (1 or 2): ")
    if choice == "1":
        quote = random.choice(quotes)
        print(f"Your quote of the day is: {quote}")
    elif choice == "2":
        print("Thank you for using the Quote Generator!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")