import multiprocessing
import random
import time
from threading import current_thread
import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops

def intense_calculation(value):
    time.sleep(random.randint(5,20))
    return value

optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

#  intenção de criar 3 processos
#  1 processo
rx.of("Alpha",
    "Beta",
    "Gamma",
    "Delta",
    "Epsilon").pipe(
                    ops.map(lambda s: intense_calculation(s)),
                    ops.subscribe_on(pool_scheduler)
                    ).subscribe(
                                on_next=lambda i: print("processo 1: {} {}".format(current_thread().name, i)),
                                on_error=lambda e: print("Erro identificado: {}".format(e)),
                                on_completed=lambda: print("Fim do processo 1!")
                                )

#  processo 2
rx.range(1,10).pipe(
                    ops.map(lambda s: intense_calculation(s)),
                    ops.subscribe_on(pool_scheduler)
                    ).subscribe(
                                on_next=lambda i: print("processo 2: {} {}".format(current_thread().name, i)),
                                on_error=lambda e: print("Erro identificado: {}".format(e)),
                                on_completed=lambda: print("Fim do processo 2!")
                                )

#  processo 3

rx.interval(1).pipe(
                    ops.map(lambda i: i*100),
                    ops.observe_on(pool_scheduler),
                    ops.map(lambda s: intense_calculation(s))
                    ).subscribe(
                                on_next=lambda i: print("processo 3: {} {}".format(current_thread().name, i)),
                                on_error=lambda e: print("Erro identificado: {}".format(e))
                                )

input("Pressione alguma tecla para sair\n")