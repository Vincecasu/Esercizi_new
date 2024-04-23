def subtract(x: float,y: float) -> float:
    return x - y

x ,y = float(input("Inserisci il primo numero: ")),\
    float(input("Inserisci il secondo numero: "))

diff = subtract(x,y)

print(f"La differenza tra {x} ed {y} è uguale a {diff}")
