import json

if __name__ == "__main__":
    data = [
        {
            "driver_name": "Fernando Alonso",
            "number": "14",
            "age": 42
        },
        {
            "driver_name": "Carlos Sainz",
            "number": "55",
            "age": 27
        },
    ]

    print(data)
    print(type(data))
    json_str = json.dumps(data)
    print(json_str)
    print(type(json_str))

    with open("pilotos.json", "w") as fichero:
        json.dump(data, fichero)

    with open("pilotos_pretty.json", "w") as fichero:
        json.dump(data, fichero, indent=4)
