def subtract_lists(x: list[float],y: list[float]) -> list[float]:
    new_list = []
    if len(x) >= len(y):
       for l in range(len(y)):
        diff: float = x[l] - y[l]
        new_list.append(diff)
    else:
       for l in range(len(x)):
          diff: float = x[l] - y[l]
          new_list.append(diff)
    return new_list

mylist: list[float]=[1,2,3,4,5,6]
y : list[float] = [2,3,4,5,6]
result = subtract_lists(mylist,y)

print(f"La differenza secondo la posizione è {result}")
          
    