from rx import disposable, create

stocks = [
    {'TCKR': 'APPL', 'PRICE': 200},
    {'TCKR': 'GOOG', 'PRICE': 90},
    {'TCKR': 'TSLA', 'PRICE': 120},
    {'TCKR': 'MSFT', 'PRICE': 150},
    {'TCKR': 'INTL', 'PRICE': 70}
]

def buy_stock_events(observer, scheduler):
    for stock in stocks:
        if(stock['PRICE'] > 100):
            observer.on_next(stock['TCKR'])
    observer.on_completed()

class StockObserver(disposable.Disposable):

    def on_next(self, value):
        print("Instruções recebidas para comprar a açao {}".format(value))

    def on_completed(self):
        print("Todas as instruções de compra foram finalizadas!")

    def on_error(self, error):
        print("Erro identificado: {}".format(error))

fonte = create(buy_stock_events)
fonte.subscribe(StockObserver())