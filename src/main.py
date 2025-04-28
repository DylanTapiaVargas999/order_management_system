# src/main.py

from order import Order
from order_repository import OrderRepository
from payment_service import PaymentService
from email_service import EmailService

def main():
    # Crear una orden
    customer_name = input("Enter customer's name: ")
    customer_email = input("Enter customer's email: ")
    items = input("Enter items separated by comma: ").split(",")
    total_amount = float(input("Enter total amount: "))

    order = Order(customer_name, customer_email, items, total_amount)

    # Crear servicios
    repo = OrderRepository()
    payment = PaymentService()
    email = EmailService()

    # Usar servicios
    repo.save(order)
    payment.process_payment(order)
    email.send_confirmation_email(order)

if __name__ == "__main__":
    main()
