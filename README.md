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


<hr> 
<div dir='rtl'>
	
## راهنما

### معرفی سرویس کاوه نگار

کاوه نگار یک وب سرویس ارسال و دریافت پیامک و تماس صوتی است که به راحتی میتوانید از آن استفاده نمایید.

### ساخت حساب کاربری

اگر در وب سرویس کاوه نگار عضو نیستید میتوانید از [لینک عضویت](http://panel.kavenegar.com/client/membership/register) ثبت نام  و اکانت آزمایشی برای تست API دریافت نمایید.

### مستندات

برای مشاهده اطلاعات کامل مستندات [وب سرویس پیامک](http://kavenegar.com/وب-سرویس-پیامک.html)  به صفحه [مستندات وب سرویس](http://kavenegar.com/rest.html) مراجعه نمایید.

### راهنمای فارسی

در صورتی که مایل هستید راهنمای فارسی کیت توسعه کاوه نگار را مطالعه کنید به صفحه [کد ارسال پیامک](http://kavenegar.com/sdk.html) مراجعه نمایید.

### اطالاعات بیشتر
برای مطالعه بیشتر به صفحه معرفی
[وب سرویس اس ام اس ](http://kavenegar.com)
کاوه نگار
مراجعه نمایید .

 اگر در استفاده از کیت های سرویس کاوه نگار مشکلی یا پیشنهادی  داشتید ما را با یک Pull Request  یا  ارسال ایمیل به support@kavenegar.com  خوشحال کنید.
 
##
![http://kavenegar.com](http://kavenegar.com/public/images/logo.png)		

[http://kavenegar.com](http://kavenegar.com)	

</div>


