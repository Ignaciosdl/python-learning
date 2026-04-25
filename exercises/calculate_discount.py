def calculate_discount(price, discount):
    return price - (price * discount / 100)

products = [
    {"name": "laptop", "price": 1000},
    {"name": "phone", "price": 500},
    {"name": "tablet", "price": 750}
]

# Escribir un loop que imprima el precio final de cada producto aplicando un descuento del 10%
discount = 10

for product in products:
    product_w_discount = calculate_discount(product["price"],discount)
    print(f"{product["name"]}: ${product["price"]} -> ${product_w_discount} after 10% discount")