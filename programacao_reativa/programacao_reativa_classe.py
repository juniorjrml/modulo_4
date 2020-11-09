from rx import create, disposable
from rx import of

def push_five_strings(observer, scheduler):
    entradas = ["Alpha",
                "Beta",
                "Gamma",
                "Delta",
                "Epsilon"]

    for entrada in entradas:
        observer.on_next(entrada)

    observer.on_completed()

class printObserver(disposable.Disposable):
    def on_next(self, value):
        print("Recebido {}".format(value))

    def on_completed(self):
        print("Fim!")

    def on_error(self, error):
        print("Erro identificado: {}".format(error))

#  cria o observable
fonte = create(push_five_strings)

#  define o observer
fonte.subscribe(printObserver())
#  outro metodo de instanciar

fonte2 = of("Alpha",
            "Beta",
            "Gamma",
            "Delta",
            "Epsilon")

fonte2.subscribe(
    on_next=lambda i: print("Recebido {}".format(i)),
    on_error=lambda e: print("Erro identificado: {}".format(e)),
    on_completed= lambda: print("Fim!")
)

