#!/usr/bin/env python
from kavenegar import *
try:
    api = KavenegarAPI('Your APIKey')
    params = {
        'receptor': '',
        'template': '',
        'token': '',
        'type': 'sms',#sms vs call
    }   
  response = api.verify_lookup(params)
  print(response)
except APIException as e: 
  print(e)
except HTTPException as e: 
  print(e)