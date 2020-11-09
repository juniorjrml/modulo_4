import threading
import time
from threading import Thread
import random


class Filosofo(Thread):

    def __init__(self, nome, garfo_direito, garfo_esquerdo):
        super().__init__(name=nome)
        print("{} sentou na mesa".format(nome))
        self.garfo_direito = garfo_direito
        self.garfo_esquerdo = garfo_esquerdo
        self.n_refeicoes = 0

    def run(self):
        def mensagem(mensagem):
            print(threading.currentThread().getName(), mensagem)

        def da_um_tempo():
            time.sleep(random.randint(1, 5))

        def pega_garfo(garfo):
            garfo.acquire()

        def solta_garfo(garfo):
            garfo.release()

        ciclo_de_vida = 10
        while ciclo_de_vida > 0:
            ciclo_de_vida -= 1

            mensagem("começou a pensar(cv = {}, n de refeicoes = {})".format(ciclo_de_vida, self.n_refeicoes))
            da_um_tempo()
            mensagem("Parou de pensar")

            try:
                pega_garfo(self.garfo_esquerdo)
                mensagem("pegou o garfo da esquerda.")
                da_um_tempo()

                try:
                    if self.garfo_direito.locked():
                        solta_garfo(self.garfo_esquerdo)
                        raise Exception

                    mensagem("tentou pegar o direito")
                    pega_garfo(self.garfo_direito)
                    mensagem("pegou os dois garfos e comecou a comer")

                    self.n_refeicoes += 1

                    solta_garfo(self.garfo_direito)
                    mensagem("soltou o garfo da direita")
                except:
                    mensagem("não pode pegar o garfo direito")

                solta_garfo(self.garfo_esquerdo)
                mensagem("soltou o garfo da esquerda")
            except:
                mensagem("não pode pegar o garfo esquerdo")


garfo1 = threading.Lock()
garfo2 = threading.Lock()
garfo3 = threading.Lock()
garfo4 = threading.Lock()
garfo5 = threading.Lock()

filosofos = []
filosofos.append(Filosofo("primeiro", garfo1, garfo2))
filosofos.append(Filosofo("segundo", garfo2, garfo3))
filosofos.append(Filosofo("terceiro", garfo3, garfo4))
filosofos.append(Filosofo("QUARTO", garfo4, garfo5))
filosofos.append(Filosofo("quinto", garfo5, garfo1))

for f in filosofos:
  f.start()

for f in filosofos:
  f.join()
