class Objekts:
    def __init__(self, nosaukums, veids):
        self.nosaukums = nosaukums
        self.veids = veids

    def paradi_informaciju(self):
        print(f"Objekts: {self.nosaukums}, Veids: {self.veids}")

class Grāmata(Objekts):
    def __init__(self, nosaukums, veids):
        super().__init__(nosaukums, veids )

    def paradi_informaciju(self):
        print(f"Grāmata: {self.nosaukums}, Veids: {self.veids}")


