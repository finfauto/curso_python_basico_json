import json
import os

if __name__ == "__main__":

    with open(os.path.join("..", "serialización", "pilotos.json"), "r") as fichero:
        data = json.load(fichero)
        print(data)
        print(type(data))

    with open(os.path.join("..", "serialización", "pilotos_pretty.json"), "r") as fichero:
        data = json.load(fichero)
        print(data)
        print(type(data))
