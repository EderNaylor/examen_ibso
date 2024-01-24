import json


def display_favorite_number():
    """program that reads in this value and prints the message, 
    “I know your favorite number! Its _____."""
    try:
        with open("json/favorite_number.json", "r") as file:
            favorite_number = json.load(file)
        print(f"I know your favorite number! Its {favorite_number}.")
    except FileNotFoundError:
        print("No favorite number found. Please run save_favNumber.py to save it.")

