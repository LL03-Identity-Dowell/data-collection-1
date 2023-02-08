# views.py
from django.shortcuts import render
import requests
import json
from datetime import datetime

def post_data(request):
    url = "http://100002.pythonanywhere.com/"
    event_id = get_event_id()
    
    payload = json.dumps({
        "cluster": "login",
        "database": "login",
        "collection": "user_profile",
        "document": "user_profile",
        "team_member_ID": "1168",
        "function_ID": "ABCDE",
        "command": "insert",
        "field": {
            "eventId" : event_id,
            "profile": {
                "first_name": "First Name",
                "last_name": "Last Name",
                "phone number": "Phone",
                "email": "email address",
                "address": "address",
                "pincode": "pincode",
                "location": "location"
            },
            "device" : {
                "phone_ID" : "phone ID",
                "phone_brand" : "phone brand"
            },
            "personal_ID" : {
                "voice_ID" : "voice id"
            },
        },
        "update_field": {
            "order_nos": 21
        },
        "platform": "bangalore"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return render(request, 'base/post_data.html', {"response": response.text})
    
def get_event_id():
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url="https://100003.pythonanywhere.com/event_creation"

    data={
        "platformcode":"FB" ,
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41",
        "login_id":"lav",
        "session_id":"new",
        "processcode":"1",
        "regional_time":time,
        "dowell_time":time,
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
    r=requests.post(url,json=data)
    return r.text

