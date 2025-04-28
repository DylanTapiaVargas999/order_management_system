# tests/test_order_services.py

import sys
import os
import unittest
from unittest.mock import patch, mock_open

# Añadir la carpeta src al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Importamos las clases que vamos a testear desde el módulo src/
from order import Order
from order_repository import OrderRepository
from payment_service import PaymentService
from email_service import EmailService


class TestOrderServices(unittest.TestCase):
    def setUp(self):
        
        # Creamos un objeto Order para usarlo en varios tests
        self.order = Order("John Doe", "john@example.com", ["Laptop", "Mouse"], 1500.0)

    # Test para verificar que los atributos de la orden están correctos
    def test_order_attributes(self):
        self.assertEqual(self.order.customer_name, "John Doe")
        self.assertEqual(self.order.customer_email, "john@example.com")
        self.assertEqual(self.order.items, ["Laptop", "Mouse"])
        self.assertEqual(self.order.total_amount, 1500.0)

    # Test para verificar que la orden se guarda correctamente en un archivo
    def test_save_order(self):
        repo = OrderRepository()
        with patch("builtins.open", mock_open()) as mocked_file:
            repo.save(self.order)
            mocked_file.assert_called_once_with("orders.txt", "a")
            handle = mocked_file()
            handle.write.assert_called_once()

    # Test para verificar que el pago de la orden se procesa correctamente
    def test_process_payment(self):
        payment = PaymentService()
        with patch('builtins.print') as mocked_print:
            payment.process_payment(self.order)
            mocked_print.assert_called_with(f"Processing payment of ${self.order.total_amount} for {self.order.customer_name}. Payment Successful!")

    # Test para verificar que el email de confirmación se envía correctamente
    def test_send_email(self):
        email = EmailService()
        with patch('builtins.print') as mocked_print:
            email.send_confirmation_email(self.order)
            mocked_print.assert_called_with(f"Sending confirmation email to {self.order.customer_email} for the order of {len(self.order.items)} items.")

    # Test para verificar cómo se maneja un pedido con ítems vacíos
    def test_order_with_empty_items(self):
        empty_order = Order("Jane Doe", "jane@example.com", [], 0.0)
        self.assertEqual(len(empty_order.items), 0)
        self.assertEqual(empty_order.total_amount, 0.0)

if __name__ == "__main__":
    unittest.main()
