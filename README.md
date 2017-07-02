# kavenegar-examples-python
## Installation
```
pip install kavenegar
```
## Usage

### Send
```python
from kavenegar import *
try:
    api = KavenegarAPI('Your APIKey')
    params = {
        'sender': '',#optional
        'receptor': '',#multiple mobile number, split by comma
        'message': '',
    } 
    response = api.sms_send(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```
### OTP
```python
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
```
### Send Bulk
```python
#!/usr/bin/env python
from kavenegar import *
try:
    api = KavenegarAPI('Your APIKey')
    params = {
        'sender':'["",""]',#array of string as json 
        'receptor': '["",""]',#array of string as json 
        'message': '["",""]',#array of string as json 
    } 
    response = api.sms_sendarray(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```
