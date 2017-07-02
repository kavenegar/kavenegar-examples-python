#!/usr/bin/env python
from kavenegar import *
try:
  api = KavenegarAPI('your apikey here')
  params = {
      'receptor': '',
      'template': '',
      'token': '',
      'token2': '',
      'token3': '',
      'type': 'sms',#sms vs call
  }   
  response = api.verify_lookup(params)
  print(response)
except APIException as e: 
  print(e)
except HTTPException as e: 
  print(e)