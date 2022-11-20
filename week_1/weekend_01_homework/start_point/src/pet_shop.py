# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

def add_or_remove_cash(petshop, number):
    petshop["admin"]["total_cash"] = get_total_cash(petshop) + number
    return get_total_cash(petshop)

def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]

def increase_pets_sold(petshop, number):
    petshop["admin"]["pets_sold"] += number

def get_stock_count(petshop):
    pets = petshop["pets"]
    return len(pets)

def get_pets_by_breed(petshop, breed):
    pets = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(petshop, name):
    for pet in petshop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(petshop, name):
    for pet in petshop["pets"]:
        if pet["name"] == name:
            petshop["pets"].remove(pet)

def add_pet_to_stock(petshop, new_pet):
    petshop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] = customer["cash"] - cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(petshop, pet, customer):
    if pet == None:
        return "pet not found"
    else:
        if customer_can_afford_pet(customer, pet) == True:
            increase_pets_sold(petshop, 1)
            add_pet_to_customer(customer, pet)
            remove_pet_by_name(petshop, pet)
            add_or_remove_cash(petshop, pet["price"])
            remove_customer_cash(customer, pet["price"])
        else:
            return "insufficient funds"
        
# def sell_pet_to_customer(petshop, pet, customer):
    
    # IF find_pet_by_name(petshop, pet) == None
    #  ---- i guess that's already assing through in the test?
    #  ----- so maybe if pet = None
    # RETURN pet not found
    # ELSE pass ?

    # IF: customer_can_afford_pet(customer, pet) == False
    # don't add pet to list, return insufficient funds
    # ELSE 
    #         add_pet_to_customer(customer, pet)
        # AND remove_pet_by_name(petshop, pet)
        # AND add_or_remove_cash(petshop, number) 
        #     but make the number the amount of cash the customer
        #     pays for the pet
        # AND remove_customer_cash(customer, cash)
        #     and remove the price of the pet from the customers cash
