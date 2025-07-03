import json
from menu import calculate_price

def build_order_prompt(menu, toppings):
    pizzas = ", ".join([f"{k} ({v}€)" for k, v in menu.items()])
    topps = ", ".join([f"{k} (+{v}€)" for k, v in toppings.items()])

    return f"""
You are an AI Pizza Assistant.
Available pizzas: {pizzas}.
Available toppings: {topps}.
Ask the user for their pizza order, any extra toppings, allergies (e.g. vegan, halal), and delivery address.
Include ONLY the menu items and topping names listed. Do not make up prices or items.
At the end, summarize the order in JSON format with keys: 'pizzas', 'toppings', 'special_requests', 'address', 'total_price'.
If anything is unclear or missing, ask again.
"""

def increment_request_count(filename="request_counter.txt"):
    try:
        with open(filename, "r") as f:
            count = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        count = 0
    count += 1
    with open(filename, "w") as f:
        f.write(str(count))
    return count

def parse_order_and_recalculate(json_response):
    try:
        order = json.loads(json_response)
        price = sum(
            calculate_price(pizza, order["toppings"]) for pizza in order["pizzas"]
        )
        order["total_price"] = price
        return order
    except Exception as e:
        return {"error": "Invalid order format"}