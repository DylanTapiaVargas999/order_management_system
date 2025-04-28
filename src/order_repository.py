# src/order_repository.py

class OrderRepository:
    # Método para guardar un pedido en un archivo de texto (orders.txt)
    def save(self, order):
        # Abre el archivo 'orders.txt' en modo "append" y escribe los detalles del pedido
        with open("orders.txt", "a") as f:
            f.write(f"Customer: {order.customer_name}, Email: {order.customer_email}, Items: {order.items}, Total: ${order.total_amount}\n")
        
        # Imprime un mensaje indicando que el pedido fue guardado correctamente
        print(f"Order for {order.customer_name} saved.")
