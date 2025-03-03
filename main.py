import serij
import extensions

print("Creating Object Dog...")
some_object = serij.Objekts(nosaukums="Dog", veids="Animal")
print("And using its function paradi_informaciju()...")
some_object.paradi_informaciju()
print("-"*32)
print("Creating Book...")
some_book = serij.Grāmata(nosaukums="Book about dogs", veids="XXX books")
print("And using its function paradi_informaciju()...")
some_book.paradi_informaciju()
print("-"*32)
print("Creating Product Dog...")
some_product = extensions.Produkts(nosaukums="Dog", veids="Animal", price=666)
print("And using its function paradi_informaciju()...")
some_product.paradi_informaciju()
print("And using its function buy()...")
some_product.buy()
print("-"*32)

