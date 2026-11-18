import json
from pathlib import Path

def validate_customer(name, phone):
    if name and phone:
        return True

    return False


def validate_product(product, products):
    if product in products:
        return True

    return False


def calculate_total(price, quantity):
    return price * quantity



def validate_quantity(quantity):
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        return False 


    if quantity < 1:
        return False

    return True 


def process_order(name, phone, product, quantity, products):
    if not validate_customer(name, phone):
        return "Invalid customer information." 

    if not validate_product(product, products):
        return "Product not available"

    if not validate_quantity(quantity):
        return "Invalid quantity"

    price = products[product]

    total = calculate_total(price, quantity)

    return {
        "customer_name": name,
        "phone": phone,
        "product": product,
        "quantity": quantity,
        "unit_price": price,
        "total": total
    }

def save_order(order):
    file_path = Path("data/orders.json")


    if file_path.exists():
        orders = json.loads(file_path.read_text())
    else:
        orders = []
    orders.append(order)
    file_path.write_text(json.dumps(orders, indent=4))

    return True


def display_confirmation(order):
    print("ORDER CONFIRMATION")
    print(f"Customer: {order['customer_name']}")
    print(f"Product: {order['product']}")
    print(f"Quantity: {order['quantity']}")
    print(f"Unit price: ₦{order['unit_price']:,}")
    print(f"Total: ₦{order['total']:,}")



def place_order(name, phone, product, quantity, products):
    order = process_order(name, phone, product, quantity, products)

    if isinstance(order, str):
        return order

    saved = save_order(order)

    if not saved:
        return "Order could not be saved."

    display_confirmation(order)
    return "Order completed successfully."