pizzas = ['Pepperoni','Cheese','Combo','Meat Lovers','Anchovies','Greek','BBQ Chicken']

for piz in pizzas:
    print(f"I like {piz.title()}\n")

print("I really love pizza, but need to have it a bit less frequently that others, so I don't become sick")

pisa = pizzas[:]
pizzas.append('Maui')

pisa.append('Veggie')

print("\n")
print("Now we are going to print two separate lists. The first is for the variable pizzas")

for ij in pizzas:
    print(f"{ij.title()}")

print("\n")
print("Now we are going to print the second list for the variable pisa")

for kj in pisa:
    print(f"{kj.title()}")

print("Done!")







