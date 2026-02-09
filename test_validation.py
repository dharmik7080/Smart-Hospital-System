from models import Person, Staff
import unittest

class TestModelValidation(unittest.TestCase):
    def test_invalid_contact(self):
        print("Testing Invalid Contact...")
        with self.assertRaises(ValueError) as cm:
            Person(1, "Test", 30, "123") # Short contact
        self.assertEqual(str(cm.exception), "Contact must be a 10-digit number")
        print("Pass: Caught short contact.")

        with self.assertRaises(ValueError) as cm:
            Person(1, "Test", 30, "abcdefghij") # Non-digit
        self.assertEqual(str(cm.exception), "Contact must be a 10-digit number")
        print("Pass: Caught non-digit contact.")

    def test_invalid_email(self):
        print("Testing Invalid Email...")
        with self.assertRaises(ValueError) as cm:
            # Valid contact (10 digits) but invalid email
            Staff(1, "Test", 30, "1234567890", "Nurse", "Day", "invalid-email", "pass")
        self.assertEqual(str(cm.exception), "Invalid Email Format")
        print("Pass: Caught invalid email.")

    def test_valid_creation(self):
        print("Testing Valid Creation...")
        try:
            s = Staff(1, "Test", 30, "1234567890", "Nurse", "Day", "test@hospital.com", "pass")
            print(f"Success: Created Staff {s.name}")
        except ValueError as e:
            self.fail(f"Valid creation failed with error: {e}")

if __name__ == "__main__":
    unittest.main()
