# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(sum):
    return sum["admin"]["total_cash"]


def add_or_remove_cash(dict,cash):
    dict["admin"]["total_cash"] += cash

def get_pets_sold (pets_sold):
 return pets_sold["admin"]["pets_sold"]

 def increase_pets_sold(pets_sold):