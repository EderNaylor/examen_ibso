import json

import json
import os

def save_favorite_number():
    """
    A program that prompts for the user's favorite number. Store this number
    in a file (json.dump()).
    """

    favorite_number = input("Please enter your favorite number: ")
    try:
        favorite_number = int(favorite_number)

        # Verificar si la carpeta 'json' existe, y si no, crearla
        folder_path = "json"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Guardar el número en un archivo dentro de la carpeta
        file_path = os.path.join(folder_path, "favorite_number.json")
        with open(file_path, "w") as file:
            json.dump(favorite_number, file)

        print("Your favorite number has been saved!")
    except ValueError:
        print("Error: Please enter numbers only.")


save_favorite_number()
