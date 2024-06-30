# def say_hello (name:str) -> None:

#     print(f"Hello, {name}")

# def say_ciao(name:str) -> None:

#     print(f"Ciao, {name}")

# def saluta(func):
#     func("Flavio")

# saluta(say_hello)
# saluta(say_ciao)

# def parent():

#     print(f"Sono in parent")

#     def first_child():

#         print(f"Sono in first child")

#     def second_child():

#         print(f"Sono in second child")
    
#     return second_child



        
# def decoretor(func):

#     def wrapper(*args):

#         import time

#         start =time.time()

#         func(*args)

#         end = time.time()
#         elapsed_time = end - start
#         print(f"{elapsed_time}")
    
#     return wrapper


# def say_hello(name: str) -> None:
#     print(f"Hello, {name}")

# say_hello = decoretor(say_hello)

# say_hello("Vincenzo")

# def say_ciao() -> None:

#     print(f"Ciao, Vincenzo")

# say_ciao = decoretor(say_ciao)

# say_ciao()


# def generatore():

#     yield "A"
#     yield "B"
#     yield "C"

# prova_generatore = generatore()
# print(next(prova_generatore))
# print(next(prova_generatore))
# print(next(prova_generatore))
# import time
# import random

# def funzione(id: int):
#     import time
#     import random

#     sleep_time:int = random.randint(1,10)
#     print(f"{id=} time {time.time()}")
#     time.sleep(sleep_time)
#     print(f"{id=} time {time.time()}")

# if __name__ == "__main__":

#     import threading
#     from concurrent.futures import ThreadPoolExecutor

#     with ThreadPoolExecutor(max_workers=10) as executor:
#         executor.map(funzione, range (10))

    # lista_thread: list[threading.Thread,] = []

    # for id in range (3):


    #     x: threading.Thread = threading.Thread(target=funzione, args=(id,))
    #     lista_thread.append(x)
    #     print(f"Prima di runnare il thread {time.time()}")
    #     x.start()
    #     print(f"Ho runnato il thread {time.time()}")

    # for t in lista_thread:

    #     t.join()
    #     print(f"Terminato!")

def decoretor(func):
    def wrapper():
        print(f"Something is happening before the function is called.")

        func()

        print(f"Something ishappening after the funcion is called.")
    
    return wrapper

def say_whee():
    print(f"Whee!")

say_whee = decoretor(say_whee)
say_whee()
    
