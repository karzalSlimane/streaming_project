import unittest
from src.producer.data_producer import send_message

class TestKafkaProducer(unittest.TestCase):

    def test_send_message(self):
        message = {"user_id": 1234, "age": 30, "location": "New York"}
        send_message(message)  # Ensure it doesn’t raise errors
        self.assertTrue(True)  # Replace with actual assertions

if __name__ == '__main__':
    unittest.main()
