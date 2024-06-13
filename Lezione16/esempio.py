reader = open("esempio.txt")
print(reader)

try:
    reader.readline()

    print("sono nella try")
    raise Exception("Eccezione!")



except Exception:
    print("sono nella exeption")


finally :
    print (reader) 

    reader.close()

    print("sono nella finally")


with open("esempio.txt") as reader:

    reader.readline()
    print(reader.readline())




