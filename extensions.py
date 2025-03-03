import random
import serij

class Produkts(serij.Grāmata):
    def __init__(self, nosaukums, veids, price):
        self.price = price
        super().__init__(nosaukums, veids)

    def paradi_informaciju(self):
        print(f"Grāmata: {self.nosaukums}, Veids: {self.veids}, Price: {self.price}")
    def buy(self):
        print(f"Price of this book is {self.price} and we give u discount {random.randint(0,60)}%")

