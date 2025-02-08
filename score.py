"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")

# FIXED
    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

import random


def determine_score(score):
    """Determine the result based on the score."""
    if score < 50:
        return "Bad"
    elif 50 <= score < 65:
        return "Passable"
    elif 65 <= score < 85:
        return "Good"
    else:
        return "Excellent"


def main():
    """Ask for a user score and generate a random score."""
    # Ask user for input score
    user_score = int(input("Enter your score (0-100): "))

    # Generate a random score between 0 and 100
    random_score = random.randint(0, 100)

    # Print results using determine_score
    print(f"Your score: {user_score} is {determine_score(user_score)}")
    print(f"Random score: {random_score} is {determine_score(random_score)}")


if __name__ == "__main__":
    main()
