def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


print("index =", index(-180, -180))
print("(-180, -180) =", xy(index(-180, -180)   ))

print("index =", index(180, -180))
print("(180, -180) =", xy(index(180, -180)))

print("index =", index(180, 180))
print("(180, 180) =", xy(index(180, 180)))

print("index =", index(180, -180))
print("(180, -180) =", xy(index(180, -180)))

alumnos = """Tere
Luis Carlos
Alexandra
Nico
Edgar
Ricardo
Miguel
Ernesto
Frida
Tabatha
Marcelo
Dani
Omar
Héctor
Iván
Enrique
Adrián
Axel
Carlo
Alejandro
Cirino
Rodrigo
Abraham
Jesús
Rubén
Roberto
Diego
Ángel
Ana
José
Andrés
'Rikardo"""
lista = alumnos.split('\n')
print(lista)
print(len(lista))
hide = [True] * 64
print(hide)

