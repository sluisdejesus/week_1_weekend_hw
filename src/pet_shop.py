# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(sum):
    return sum["admin"]["total_cash"]


def add_or_remove_cash(dict,cash):
    dict["admin"]["total_cash"] += cash

def get_pets_sold (pets_sold):
 return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
     pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(get_breed, breed):
    breed_count = []
    for pet in get_breed["pets"]:
        if pet["breed"] == breed:
             breed_count.append(breed)
    return breed_count

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

def remove_pet_by_name(pet_shop, name):
    name_removed =[]
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            name_removed = pet_shop["pets"].index(pet)
    pet_shop["pets"].pop(name_removed)

def add_pet_to_stock (add_stock, pet):
    add_stock["pets"].append(pet)

def get_customer_cash(customer):
    return customer["cash"]
    
def remove_customer_cash(customer,cash):
    customer ["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer,new_pet):
    customer["pets"].append(new_pet)