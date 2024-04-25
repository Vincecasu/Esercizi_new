def add_diff_to_res(x: list[float], y: list[float], length: int) -> list[float]:
    res: float = []
    for i in range(length):
        diff: float = x[i] - y[i]
        res.append(diff)
    return res

def subtract_lists(x: list[float], y: list[float]) -> list[float]:
    length = min(len(x), len(y))
    res: list[float] = add_diff_to_res(x,y,length)
    return res

mylist: list[float]=[1,2,3,4,5]
y: list[float] = [2,3,4,5,6]
result: list[float] = subtract_lists(mylist,y)

print(f"Il risultato della sottrazione è {result}")