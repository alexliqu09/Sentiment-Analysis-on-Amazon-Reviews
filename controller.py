from model import BERT


def Singleton(cls):
    istances = dict()

    def wrap(*args, **kwargs):
        if cls not in istances:
            istances[cls] = cls(*args, **kwargs)
        return istances[cls]

    return wrap


@Singleton
class Controller:
    def __init__(self):
        self.beto = BERT(
            3, 200, "dccuchile/bert-base-spanish-wwm-cased", "Betoweight.pth"
        )
        self.mbert = BERT(3, 200, "bert-base-multilingual-cased", "MBertweight.pth")

    def prediction(self, frase, opt):
        if opt == "beto":
            return self.beto.sentiment_classification(frase)
        elif opt == "mbert":
            return self.mbert.sentiment_classification(frase)

        else:
            return "Model not Available"


controller = Controller()
