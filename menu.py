menu = {
    "Margherita": 5,
    "Pepperoni": 6,
    "Vegan Delight": 7,
    "BBQ Chicken": 7,
    "Mushroom": 4,
    "Tuna": 5,
    "Four Cheese": 6,
    "Chicken Burst": 8
}

toppings = {
    "extra cheese": 1,
    "olives": 1,
    "onions": 1,
    "jalapenos": 1,
    "mushrooms": 1
}

def calculate_price(pizza_name, selected_toppings):
    base_price = menu.get(pizza_name, 0)
    topping_price = sum(toppings.get(t, 0) for t in selected_toppings)
    return base_price + topping_price