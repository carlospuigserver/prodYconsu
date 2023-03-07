import queue
import threading
import time

colaCajas=queue.Queue(maxsize=10)

def produccionCaja():
    time.sleep(2)
    return f"Caja {time.time()}"

def empacarProducto(caja,producto):
    time.sleep(2)
    print("Se han empacado ",producto," en la caja ",caja)

def productora():
    while True:
        caja=produccionCaja()
        try:
            colaCajas.put(caja,block=False)
            print("Se está produciendo la ",caja)
        except queue.Full:
            print("La cola está llena, tendrás que esperar")
            time.sleep(2)

def empleados():
    while True:
        try:
            caja=colaCajas.get(block=False)
            empacarProducto(10,caja) # 10 es el número de productos que se van a empacar en la caja
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
