"""Validates Zambian mobile numbers"""
import json
import os

def load_zambia_data():
  """Loads phone number data from data/zambia.json

  Returns:
      A dictionary containing phone number prefix data for Zambia.
  """
  pass
data = {
      "airtel": ['97', '77'],
      "mtn": ['96', '76'],
      "zamtel": ['95'],
  }
    
def get_ip_code(number: str) -> str:
    code = ''
    if len(number) == 10:
        code = number[1:3]
    elif len(number) == 12:
        code = number[3:5]
    return code

class ZambiaValidators():
    def __init__(self):
        self.area_code = '260'

    def is_number_len_valid(self, number:str) -> bool:
        """
        validates the length of the phone number, returns True if valid
        otherwise returns False.
        """
        if not number.isdigit():
            raise ValueError("Number must be digits only.")
        else:
            if len(number) == 10 or len(number) == 12:
                return True
            else:
                return False

    def get_network_provider(self, number: str) -> str:
        """
        Gets the first thre digits of the number and searches for the
        network provider in the json data.
        Returns network provider if found, else returns Not a valid
        Zambian number.
        """
        # Validate number length
        is_len_valid = self.is_number_len_valid(number)
        
        if is_len_valid == False:
            return "Not a valid number."
        else:
            code = get_ip_code(number)
            for key, value_list in data.items():
                if code in value_list:
                    return key
                else:
                    return "Provider not found."

            
