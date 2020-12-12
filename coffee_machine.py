# Number of Coffee drinks
try:
    num = int(input("Write how many cups of coffee you will need:"))
    print(f"For {num} cups of coffee you will need:")
    print(f"{num*200} ml of water")
    print(f"{num*50} ml of milk")
    print(f"{num*15} g of coffee beans")
except ValueError:
    print('Enter a Number')
