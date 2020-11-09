import multiprocessing
import threading
import time
from threading import Thread

print(multiprocessing.cpu_count())


# Uma função que execute um pouco mais devagar
def coisa_mais_lenta():
    for i in range(1000):
        print(".", end="\t")


# Função para executar como decorator e medir o tempo
def tempo_decorrido(acao):
    def wrapper(numero):
        inicio = time.time()
        acao(numero)
        fim = time.time()
        print("", end='\n')
        print("[{funcao}] Tempo total de execução: {tempo_total}".format(
                funcao=acao.__name__,
                tempo_total=str(fim - inicio), end='\n'))
    return wrapper


@tempo_decorrido  # utilizando o decorator
def fazer_sequencial(vezes):
    for i in range(vezes):  # fazendo n vezes a coisa mais lenta de forma sequencial
        coisa_mais_lenta()


@tempo_decorrido  # o mesmo ^
def usar_thread(n):  # utilizanod threads para executar algo que e mais lento de forma concorrente
    threads = []
    for i in range(n):  # fazendo n vezes a coisa mais lenta usando threads
        thread = threading.Thread(target=coisa_mais_lenta)
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()


n = 10  # passando o mesmo tamanho para manter uma "igualdade"
#fazer_sequencial(n)
#usar_thread(n)


class MinhaClasseThread(Thread):
  def __init__(self, nome, thread_id, contador, processo):
    self.thread_id = thread_id
    self.nome = nome
    self.contador = contador
    super().__init__()


  # Chamanda quando é chamado o metodo start()
  def run(self):
    while(self.contador > 0):
      self.contador = processo(self.contador, self.nome, self.thread_id)


def processo(contador, nome, id):
  print("Id: {} | Nome: {} | Contador: {}".format(id, nome, contador-1))
  return contador-1


threads = []
threads.append(MinhaClasseThread("jao", 1, 10, processo))
threads.append(MinhaClasseThread("maria", 2, 20, processo))

for i in threads:
  i.start()

for i in threads:
  i.join()