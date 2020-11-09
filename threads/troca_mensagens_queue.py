from queue import Queue
from threading import Thread
import threading
import random

def produtor(fila_para_insercao, tempo_de_vida = 100):
    while tempo_de_vida > 0:
        print(tempo_de_vida, "produtor")
        fila_para_insercao.put(tempo_de_vida)
        fila_para_insercao.join()
        tempo_de_vida -= 1


def consumidor(fila_para_retirada, tempo_de_vida = 100):
    while tempo_de_vida > 0:
        dado = fila_para_retirada.get()
        print("Dado retirado = {} por {} | tempo de vida  = {}".format(dado, threading.currentThread().getName(), tempo_de_vida))
        fila_para_retirada.task_done()
        tempo_de_vida -= 1


fila = Queue()
trabalhadores = [Thread(target=produtor, args=(fila, ))]

for c in range(6):
    trabalhadores.append(Thread(target=consumidor, args=(fila, random.randint(10,20))))


for t in trabalhadores:
    t.start()

for t in trabalhadores:
    t.join()
