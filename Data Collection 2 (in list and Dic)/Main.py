import json
from django.db import models
import requests
from datetime import datetime
# putting each class of the dictionary inside a list


get_event_id={}
data= {
    "cluster": "login",
    "database": "login",
    "collection": "user_profile",
    "document": "user_profile",
    "team_member_ID": "1168",
    "function_ID": "ABCE",
    "command": "insert",
    "field": {
        "eventId" : get_event_id(),
        "profile": {
            "first_name": "First_name",
            "last_name": "Last_name",
            "Phone_number": "Phone_number",
            "email": "email address",
            "address": "address",
            "pincode": "pincode",
            "location": "location",
        },
        "device": {
            "phone_id": "phone ID",
            "phone_brand": "phone_brand",
        },
        "personal_ID": {
            "voice_ID" :"voice id"
        },
        },
        "Go to them it the city on or before they are going with them, so as to be able to get them all set, so it wont be abe to them done"
        "update_field": {
            "order_nos": 21
        },
        "plaform": "bangalore"
    }

# Creating list for each of the classes
cluster_list= [data['cluster']]
database_list= [data['database']]
collection_list= [data['collection']]
document_list= [data['document']]
team_member_ID_list= [data['team_member']]
function_ID_list= [data['function_ID']]
command_list= [data['command']]
field_list=[data['field']]
update_field_list=[data['update_field']]
platform_list=[data['platform']]


# Printing out the list
print(cluster_list)
print(database_list)
print(collection_list)
print(document_list)
print(team_member_ID_list)
print(function_ID_list)
print(command_list)
print(field_list)
print(update_field_list)
print(platform_list)



# To be in the model.py
class Userprofile(models.Model):
    cluster=models.CharField(max_length=20, choices=cluster_list)
    database=models.CharField(max_length=20, choices=database_list)
    collection=models.CharField(max_length=20, choices=collection_list)
    document=models.CharField(max_length=20, choices=document_list)
    team_member_ID=models.CharField(max_length=20, choices=team_member_ID_list)
    function_ID=models.CharField(max_length=20, choices=function_ID_list)
    command=models.CharField(max_length=20, choices=command_list)
    field=models.CharField(max_length=20, choices=field_list)
    update_field=models.CharField(max_length=20, choices=update_field_list)
    platform=models.CharField(max_length=20, choices=platform_list)
