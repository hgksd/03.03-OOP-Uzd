import random
import serij
import pandas
from colorama import Fore, Back, Style

print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

class Produkts(serij.Grāmata):
    def __init__(self, nosaukums, veids, price):
        self.price = price
        super().__init__(nosaukums, veids)

    def paradi_informaciju(self):
        """
        Displays information about object
        """
        print(Fore.YELLOW + f"Grāmata: {self.nosaukums} {Fore.WHITE}, Veids: {self.veids}, {Back.RED} Price: {self.price} {Back.BLACK}")
    
    def buy(self):
        """
        Displays price and gives u(sic) a random discount
        """
        print(f"Price of this book is {Back.RED} {self.price}  {Back.BLACK} and we give u discount  {Back.GREEN} {Style.DIM} {random.randint(0,60)}% {Style.BRIGHT} {Back.BLACK}")

