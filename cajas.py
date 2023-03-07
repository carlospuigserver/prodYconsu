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


