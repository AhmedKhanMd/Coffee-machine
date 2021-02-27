# Write your code here

# procedure to make coffee

# print("Starting to make a coffee")

# print("Grinding coffee beans")

# print("Boiling water")

# print("Mixing boiled water with crushed coffee beans")

# print("Pouring coffee into the cup")

# print("Pouring some milk into the cup")

# print("Coffee is ready!")

# quantity required for one coffee cup

coffee_items = {"water": 200, "milk": 50, "beans": 15}

# getting available quantity from users

print("Write how many ml of water the coffee machine has:") 

water_available = int(input()) # amount of water available

print("Write how many ml of milk the coffee machine has:")

milk_available = int(input())  # amount of milk available

print("Write how many gm of beans the coffee machine has:")

beans_available = int(input())

# number of cups required for users

print('Write how many cups of coffee you will need:')

cups_needed = int(input())

water_needed = coffee_items["water"] 

milk_needed = coffee_items["milk"] 

beans_needed = coffee_items["beans"]

i = 1

while True:
    
    if water_needed * i > water_available or milk_needed * i > milk_available or beans_needed * i > beans_available:
        break
    else:
        i += 1


available_cups = i - 1 

if available_cups < cups_needed:
    
    print(f'No, I can make only {available_cups} cups of coffee')

elif available_cups > cups_needed:
    
    print(f'Yes, I can make that amount of coffee (and even {available_cups - cups_needed} more than that)')
    
else:
    
    print('Yes, I can make that amount of coffee')
    
    


# print(f'For {cups_needed} cups of coffee you will need:')
# print(f'{water_needed} ml of water')
# print(f'{milk_needed} ml of milk')
# print(f'{beans_needed} g of coffee beans')