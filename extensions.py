import random
import serij

class Produkts(serij.Grāmata):
    def __init__(self, nosaukums, veids, price):
        self.price = price
        super().__init__(nosaukums, veids)

    def paradi_informaciju(self):
        """
        Displays information about object
        """
        print(f"Grāmata: {self.nosaukums}, Veids: {self.veids}, Price: {self.price}")
    
    def buy(self):
        """
        Displays price and gives u(sic) a random discount
        """
        print(f"Price of this book is {self.price} and we give u discount {random.randint(0,60)}%")

