# src/payment_service.py

class PaymentService:
    # Método para simular el procesamiento de un pago para una orden
    def process_payment(self, order):
        # Imprime un mensaje simulando el procesamiento y éxito del pago
        print(f"Processing payment of ${order.total_amount} for {order.customer_name}. Payment Successful!")
