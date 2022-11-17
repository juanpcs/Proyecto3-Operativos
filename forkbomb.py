import os 
from time import sleep, perf_counter

#numero de procesos = 2^n, con n = i

#Función que ejecuta la bomba
#Esta crea procesos exponencialmente hasta llegar al límite del ciclo establecido
def fork_bomb():
    i = 0
    while i < 30:
        
        os.fork()
        print("Proceso #"+str(os.getpid())+"\n")
        print("Esperando 1.5 S")
        sleep(1.5)
        i += 1


start_time = perf_counter()
fork_bomb()
end_time = perf_counter()
# Finaliza el conteo del tiempo
print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')

