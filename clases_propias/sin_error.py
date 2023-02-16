import json


class Piloto:
    def __init__(self, nombre, numero, edad):
        self.__nombre = nombre
        self.__numero = numero
        self.__edad = edad

    def to_serializable(self):
        return {
            "nombre": self.__nombre,
            "numero": self.__numero,
            "edad": self.__edad
        }

    @classmethod
    def from_json(cls, data):
        return Piloto(data["nombre"], data["numero"], data["edad"])


if __name__ == "__main__":
    data = [
        Piloto("Fernando Alonso", "14", 42),
        Piloto("Carlos Sainz", "55", 27)
    ]

    print(data)
    print(type(data))

    pilotos = []
    for piloto in data:
        pilotos.append(piloto.to_serializable())

    json_str = json.dumps(pilotos)
    print(json_str)
    print(type(json_str))

    data = json.loads(json_str)
    print(data)
    print(type(data))
    for entrada in data:
        print(entrada)
        print(type(entrada))
        piloto = Piloto.from_json(entrada)
        print(piloto)

