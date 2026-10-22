def laptop():
    dell = 60000
    hp = 70000
    lenovo = 80000
    
    user_input = input("Enter the laptop brand (dell, hp, lenovo): ").lower()
    
    if user_input == "dell":
        print("Your dell laptop's price is:", dell)
    elif user_input == "hp":
        print("Your hp laptop's price is:", hp)
    elif user_input == "lenovo":
        print("Your lenovo laptop's price is:", lenovo)
    else:
        print("Invalid brand entered.")

laptop()