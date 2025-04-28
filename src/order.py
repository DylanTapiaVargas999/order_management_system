# src/order.py

class Order:
    # Constructor para inicializar una orden con los detalles del cliente, los productos y el monto total
    def __init__(self, customer_name, customer_email, items, total_amount):
        self.customer_name = customer_name 
        self.customer_email = customer_email 
        self.items = items 
        self.total_amount = total_amount
