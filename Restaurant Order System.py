menu = {'burger': 10.99, 'fries': 4.99, 'soda': 1.99}
revenue = 0

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def take_order():
    order = {}
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item == 'done':
            break
        if item not in menu:
            print("Invalid item.")
            continue
        quantity = int(input("Enter quantity: "))
        order[item] = quantity
    return order

def process_order(order):
    total_price = sum(menu[item] * quantity for item, quantity in order.items())
    global revenue
    revenue += total_price
    return total_price

def display_receipt(order, total_price):
    print("Receipt:")
    for item, quantity in order.items():
        price = menu[item] * quantity
        print(f"{item}: {quantity} x ${menu[item]:.2f} = ${price:.2f}")
    print(f"Total: ${total_price:.2f}")

while True:
    display_menu()
    order = take_order()
    total_price = process_order(order)
    display_receipt(order, total_price)
    print(f"Revenue: ${revenue:.2f}")
