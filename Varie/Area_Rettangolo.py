def area_rettangolo(x: float,y: float) -> float:
    area = x * y
    return area

def calc_num_mattoni(x: float) -> int:
    num_mattoni: int = int((x // 2 % 4 +10)* 6)
    return num_mattoni

x , y = 2 , 3

out: float = area_rettangolo(x,y)

print(f"L'area del rettangolo con x = {x}" \
      + f" e y = {y} è {out}")

num_mattoni: int = calc_num_mattoni(out)

print(f"Per un'area di {out}m2 servono {num_mattoni} mattoni")