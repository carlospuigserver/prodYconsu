# prodYconsu

El link de este repositorio es el siguiente: https://github.com/carlospuigserver/prodYconsu.git

En este ejercicio, he llevado a cabo el programa de productores y consumidores, el cual es un buen ejercicio de la programación concurrente. En mi programa he utilizado el módulo queue y threading. Concretamente simula la producción y el empaquetado de productos de una fábrica, utilizando hilos y una cola para controlar ambos.

El código es el siguiente:


```
import queue
import threading
import time

colaCajas=queue.Queue(maxsize=10)
numero_cajas=1

def produccionCaja():
    time.sleep(2)
    return f"Caja {numero_cajas}"

def empacarProducto(producto,caja):
    time.sleep(2)
    print("Preparando", caja,"hay", producto,"productos, empaquetamos 10, sobran", producto-10)

def productora():
    global numero_cajas
    while True:
        if numero_cajas>10:
            break
        caja=produccionCaja()
        try:
            colaCajas.put(caja,block=False)
            print("Se está produciendo la  ",caja)
            numero_cajas+=1
        except queue.Full:
            print("La cola está llena, tendrás que esperar")
            time.sleep(2)


def empleados():
    while True:
        try:
            caja=colaCajas.get(block=False)
            empacarProducto(15,caja) #15 es el número de productos que se van a empacar en cada caja
        except queue.Empty:
            print("La cola está vacía, tendrás que esperar")
            time.sleep(2)



# Creamos los hilos

hiloProductora=threading.Thread(target=productora)
hiloEmpleados=threading.Thread(target=empleados)

hiloProductora.start()
hiloEmpleados.start()

hiloProductora.join()
hiloEmpleados.join()
```
<img width="907" alt="cajas" src="https://user-images.githubusercontent.com/91721643/223423159-285251bd-cf9d-452c-90f6-ad81a95e0784.png">




