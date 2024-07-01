products = ["t-shirt", "mug", "hat", "book", "keychain"]

inventory = dict()

for product in products:
    value = int(input(f"¿Cuántos {product} hay disponible en el inventario? -> "))
    inventory[product] = value

customer_orders = set()
for i in range(3):
    product = input('¿Qué producto quieres añadir? "t-shirt", "mug", "hat", "book" or "keychain" -> ')
    customer_orders.add(product)
print(customer_orders)

total_products = sum(inventory.values())

order_status = [len(customer_orders), (len(customer_orders) / total_products) * 100]
print(f"Order Stadistics: \n Total Products Ordered: {order_status[0]}\n Percentage of Products Ordered: {order_status[1]}%")
for key, value in inventory.items():
    inventory[key] = value-1

for key, value in inventory.items():
    print(key, " : ", value)
