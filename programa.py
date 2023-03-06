import queue
import threading
import time

# Creamos una cola
cola=queue.Queue(maxsize=5)

def produccion():
    time.sleep(2)
    return f"Producto{time.time()}"

def consumicion(producto):
    time.sleep(2)
    print("Consimuendo, ", producto)

def productor():
    while True:
        producto=produccion()
        try:
            cola.put(producto)
            print("Produciendo, ",producto)
        except queue.Full:
            print("La cola está llena, tendrás que esperar")
            time.sleep(2)



