import requests
from datetime import datetime

def get_event_id():
    url= "https://100003.pythonaywhere.com/event_creation"

    current_time= datetime.now().strftime("%d:%m:Y, %H:%M:%S")

    data={
        "platformcode":"FB",
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41",
        "login_id":"lav",
        "session_id":"new",
        "processcode":"1",
        "regional_time":current_time,
        "dowell_time":current_time,
        "location":"22446576",
        "objectcode":"1",
        "instancecode":"100051",
        "context":"afdafa ",
        "document_id":"3004",
        "rules":"some rules",
        "status":"work",
        "data_type": "learn",
        "purpose_of_usage": "add",
        "colour":"color value",
        "hashtags":"hash tag alue",
        "mentions":"mentions value",
        "emojis":"emojis",
    }
    
    response= requests.post(url, json=data)
    return response.text












