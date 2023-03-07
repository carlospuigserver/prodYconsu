# prodYconsu

El link de este repositorio es el siguiente: https://github.com/carlospuigserver/prodYconsu.git

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

<img width="912" alt="consu" src="https://user-images.githubusercontent.com/91721643/223271140-1a76fa81-e66e-4cee-b6d6-b60c94abadac.png">







Ahora llevaré a cabo un ejemplo más cuotidiano para que se entienda mejor el programa:
