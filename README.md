# prodYconsu

El link de este repositorio es el siguiente:

En este ejercicio, he llevado a cabo el programa de productores y consumidores, el cual es un buen ejercicio de la programación concurrente. En mi programa he utilizado el módulo queue, y threading, ya que he tenido que utilizar hilos para poder llevarlo a cabo. El código es el siguiente:

```
import queue
import threading
import time

# Creamos una cola
cola=queue.Queue(maxsize=5)

def produccion():
    time.sleep(2)
    return f"Producto  {time.time()}"

def consumicion(producto):
    time.sleep(2)
    print("Consumiendo ", producto)

def productor():
    while True:
        producto=produccion()
        try:
            cola.put(producto,block=False)
            print("Produciendo ",producto)
        except queue.Full:
            print("La cola está llena, tendrás que esperar")
            time.sleep(2)

def consumidor():
    while True:
        try:
            producto=cola.get(block=False)
            consumicion(producto)
        except queue.Empty:
            print("La cola está vacía, tendrás que esperar")
            time.sleep(2)


# Creamos los hilos

hiloProductor=threading.Thread(target=productor)
hiloConsumidor=threading.Thread(target=consumidor)

hiloProductor.start()
hiloConsumidor.start()

hiloProductor.join()
hiloConsumidor.join()
```

