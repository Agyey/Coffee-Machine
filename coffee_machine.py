try:
    # Amount of water
    water = int(input("Write how many ml of water the coffee machine has:"))
    # Amount of milk
    milk = int(input("Write how many ml of milk the coffee machine has:"))
    # Amount of coffee beans
    coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
    # Number of Coffee drinks
    num = int(input("Write how many cups of coffee you will need:"))
    print(f"For {num} cups of coffee you will need:")
    total_cups = min(water // 200, milk // 50, coffee // 15)
    extra_cups = total_cups - num
    if total_cups >= num:
        if extra_cups:
            print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
        else:
            print("Yes, I can make that amount of coffee")
    else:
        print(f"No, I can make only {total_cups} cups of coffee")
except ValueError:
    print('Enter a Number')
