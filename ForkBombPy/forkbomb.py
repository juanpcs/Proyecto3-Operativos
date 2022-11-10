import os 
import filterimg

def fork_bomb():
    #numero de procesos = 2^n, con n = cantidad de forks
    os.fork()
    os.fork()
    #os.fork()
    print("hello world\n")
    filterimg.ejecutar()

fork_bomb()

