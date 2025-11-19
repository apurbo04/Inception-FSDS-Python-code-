menu = {
    "coffee": 2,
    "pasta": 3,
    "Pizza": 5,
    "burger": 6,
    "Chiken": 10
}

print(    
    """
    Welcome to Apurbo,s kitchen: 
    
    coffee: $2
    pasta: $3
    Pizza: $5
    burger: $6
    Chiken: $10
    """
)

item1 = input("what you want: ")

total_price = 0

if item1 in menu:
    total_price += menu[item1]
    print(f"You ordered {item1}. your total bill is ${total_price}")

else:
    print("Invalid item, Please order something from the Menu")
    
another_order = input("Do you want to add another?(Yes/No): ").lower()

if another_order == "yes":
    item2 = input("what you want more: ")
    if item2 in menu:
        total_price += menu[item2]
        print(f"You ordered {item2}.")
    else:
        print("Invalid item, Please order something from the Menu")
        

print(f"Your total bill is ${total_price}, Thank you!")