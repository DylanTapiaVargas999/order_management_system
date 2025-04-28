# src/email_service.py

class EmailService:
    # Método para simular el envío de un correo de confirmación de pedido
    def send_confirmation_email(self, order):
        # Imprime un mensaje simulando el envío de un correo con el email del cliente y el número de ítems del pedido
        print(f"Sending confirmation email to {order.customer_email} for the order of {len(order.items)} items.")
