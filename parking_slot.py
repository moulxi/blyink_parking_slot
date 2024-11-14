import requests
import re
import urllib.parse

class SlotGroupError(Exception):
    pass


class SlotGroup:
    
    def __init__(self, token:str):
        self.token = token
    
    def send_led_sig(self, pin:str, sig:int):

        # verify if "pin" is valid
        pattern = r"^v[0-9]$"
        if not isinstance(pin, str) or not re.match(pattern, pin):
            raise SlotGroupError("send_led_sig(pin, sig), v_pin must be 'v0', 'v1', ..., 'v9' of type 'str'")
        
        # verify if "sig" is valid
        if not isinstance(sig, int) or sig not in (0, 1):
            raise SlotGroupError("send_led_sig(pin, sig), sig must be 0 or 1 of type 'int'")

        # send the signal by get method
        url = f'https://blynk.cloud/external/api/update?token={self.token}&{pin}={sig}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'Sent {sig} to {pin}')
            else:
                print(f'Failed to send the signal： {response.status_code},  {response.text}')
        except requests.exceptions.RequestException as e:
            print(f'Somthing went wrong while sending a request : {e}')
    
    def send_label_sig(self, pin:str, sig:int):
        
        # verify if "pin" is valid
        pattern = r"^v[0-9]$"
        if not isinstance(pin, str) or not re.match(pattern, pin):
            raise SlotGroupError("send_led_sig(pin, sig), v_pin must be 'v0', 'v1', ..., 'v9' of type 'str'")
        
        # verify if "sig" is valid
        if not isinstance(sig, int) or (sig < 0):
            raise SlotGroupError("send_led_sig(pin, sig), sig must be 0 or 1 of type 'int'")
        
        # send the signal by get method
        url = f'https://blynk.cloud/external/api/update?token={self.token}&{pin}={str(sig)}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'Sent {sig} to {pin}')
            else:
                print(f'Failed to send the signal： {response.status_code},  {response.text}')
        except requests.exceptions.RequestException as e:
            print(f'Somthing went wrong while sending a request : {e}')

    