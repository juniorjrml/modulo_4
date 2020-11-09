import time
from threading import Thread
import threading
import random


class VendedorPassagem(Thread):
    passagens_disponiveis = 200

    def __init__(self, nome, semaforo):
        super().__init__(name=nome)
        self.semaforo = semaforo
        self.passagens_vendidas = 0

    def run(self):
        rodando = True
        while rodando:
            self.da_um_tempo()

            self.semaforo.acquire()

            if self.get_passagens() <= 0:
                rodando = False
            else:
                self.passagens_vendidas += 1
                self.vender_passagem()

            self.semaforo.release()
        print("{} vendeu {} passagens".format(self.name, self.passagens_vendidas))

    def da_um_tempo(self):
        time.sleep(random.randint(0, 4) / 4)

    @classmethod
    def vender_passagem(cls):
        cls.passagens_disponiveis -= 1

    def get_passagens(self):
        return self.passagens_disponiveis


semaforo = threading.Semaphore()
nomes_vendedores = ["Joao", "Julia", "Roberto", "Paulo", "Fernanda", "Vitoria"]

vendedores = []
VendedorPassagem.passagens_disponiveis = 100
for v in nomes_vendedores:
    vendedor = VendedorPassagem(v, semaforo)
    vendedor.start()
    vendedores.append(vendedor)

for v in vendedores:
    v.join()
