import json


class Piloto:
    def __init__(self, nombre, numero, edad):
        self.__nombre = nombre
        self.__numero = numero
        self.__edad = edad


if __name__ == "__main__":
    data = [
        Piloto("Fernando Alonso", "14", 42),
        Piloto("Carlos Sainz", "55", 27)
    ]

    print(data)
    print(type(data))
    json_str = json.dumps(data)
    print(json_str)
    print(type(json_str))


