# Write your code here
print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")

coffee_items = {"water": 200, "milk": 50, "beans": 15}

print('Write how many cups of coffee you will need:')

cups_needed = int(input())

water_needed = coffee_items["water"] * cups_needed
milk_needed = coffee_items["milk"] * cups_needed
beans_needed = coffee_items["beans"] * cups_needed

print(f'For {cups_needed} cups of coffee you will need:')
print(f'{water_needed} ml of water')
print(f'{milk_needed} ml of milk')
print(f'{beans_needed} g of coffee beans')