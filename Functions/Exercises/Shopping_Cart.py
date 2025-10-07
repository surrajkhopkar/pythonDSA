def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost

cart = [
    {'name':'Apple','price':0.5,'quantity':5},
    {'name':'Banana','price':1.5,'quantity':12},
    {'name':'Orange','price':2.5,'quantity':8},
    {'name':'Kiwi','price':3.5,'quantity':9}
]

print(calculate_total_cost(cart))