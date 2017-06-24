#!/usr/bin/env python
from kavenegar import *
try:
    api = KavenegarAPI('Your APIKey')
    params = {
        'receptor': '',
        'message': ''
    }   
  response = api.call_maketts(params)
  print(response)
except APIException as e: 
  print(e)
except HTTPException as e: 
  print(e)