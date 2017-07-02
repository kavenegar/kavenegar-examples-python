from kavenegar import *
try:
    api = KavenegarAPI('your apikey here')
    params = {
        'sender': '',#Array of String
        'receptor': '',#Array of String
        'message': '',#Array of String
    } 
    response = api.sms_sendarray(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)