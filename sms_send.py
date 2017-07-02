from kavenegar import *
try:
    api = KavenegarAPI('your apikey here')
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