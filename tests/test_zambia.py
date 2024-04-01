import os
import unittest
from src.validators.zambia import ZambiaValidators, get_ip_code


class ZambiaValidatorsMethods(unittest.TestCase):
    """Test methods and functions for Zambia validators"""
    def setUp(self) -> None:
        self.zed = ZambiaValidators()
        return super().setUp()
    
    def test_get_ip_code(self):
        """Test getting the Provider code"""
        number1 = '0966773399' # 10 digits valid
        number2 = '260977224433' # 12 digists valid

        res1 = get_ip_code(number1)
        res2 = get_ip_code(number2)

        self.assertEqual(res1, '96')
        self.assertEqual(res2, '97')
    
    def test_valid_number_length(self):
        """Test that the method correctly validates the numbers"""
        number1 = '0966773399' # 10 digits valid
        number2 = '260977224433' # 12 digists valid
        number3 = '1234567890' # 10 digits valid

        res1 = self.zed.is_number_len_valid(number1)
        res2 = self.zed.is_number_len_valid(number2)
        res3 = self.zed.is_number_len_valid(number3)
        self.assertEqual(res1, True)
        self.assertEqual(res2, True)
        self.assertEqual(res3, True)

    def test_invalid_length(self):
        """Test that the method correctly validates the numbers"""
        number1 = '0973399'
        number2 = '260977224434553'
        number3 = '260'

        res1 = self.zed.is_number_len_valid(number1)
        res2 = self.zed.is_number_len_valid(number2)
        res3 = self.zed.is_number_len_valid(number3)
        self.assertEqual(res1, False)
        self.assertEqual(res2, False)
        self.assertEqual(res3, False)

    def test_invalid_arguments(self):
        number1 = 'mynumber'
        number2 = '0966number'
        with self.assertRaises(ValueError, msg="Number must be digits only."):
            self.zed.is_number_len_valid(number1)
        with self.assertRaises(ValueError, msg="Number must be digits only."):
            self.zed.is_number_len_valid(number2)
        with self.assertRaises(ValueError, msg="Not a valid number."):
            self.zed.get_network_provider(number1)

    def test_zamtel_mobile_numbers(self):
        """Validate ZAMTEL mobile numbers"""
        number1 = '0955556677'
        number2 = '09505556677'
        res1 = self.zed.get_network_provider(number1)
        res2 = self.zed.get_network_provider(number2)
        self.assertEqual(res1, 'zamtel')
        self.assertEqual(res2, 'Not a valid number.')

    def test_mtn__mobile_numbers(self):
        """Validates MTN Zambia numbers"""
        number1 = '260965602023'
        number2 = '0765556677'
        res1 = self.zed.get_network_provider(number1)
        res2 = self.zed.get_network_provider(number2)
        self.assertEqual(res1, 'mtn')
        self.assertEqual(res2, 'mtn')

    def test_airtel_mobile_numbers(self):
        """Validates AIRTEL Zambia numbers"""
        number1 = '0977556677'
        number2 = '0775556677'
        res1 = self.zed.get_network_provider(number1)
        res2 = self.zed.get_network_provider(number2)
        self.assertEqual(res1, 'airtel')
        self.assertEqual(res2, 'airtel')
        
    
if __name__ == "__main__":
    unittest.main()