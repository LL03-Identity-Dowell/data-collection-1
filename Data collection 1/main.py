from django.db import models
# from .models import MyModel

# Create your models here.

class My_Profile(models.Model):
    Your_first_name= models.CharField(max_length=30, blank=True)
    Your_last_name= models.CharField(max_length=30, blank=True)
    Your_phone_number= models.CharField(max_length=30, blank=True)
    Your_email= models.EmailField(unique=True)
    Your_address= models.CharField(max_length=100,blank=True) 
    pin_code= models.CharField(max_length=20, blank=True)
    Your_location=models.CharField(max_length=100, blank=True)

    Country_CHOICES=[
        ('Country 1', 'Country 1'),
        ('Country 2', 'Country 2'),
    ]
    Your_country= models.CharField(max_length=2, choices=Country_CHOICES)


    designation= models.CharField(max_length=50, blank=True)
    Your_team_code= models.CharField(max_length=20, blank=True)

    Native_language_CHOICES=[
        ('English', 'English'),
        ('Chinese', 'Chinese'),
    ]
    Your_native_language= models.CharField(max_length=2, choices=Native_language_CHOICES)

    Nationality_CHOICES=[
        ('English', 'English'),
        ('Chinese', 'Chinese'),
    ]
    Your_nationality= models.CharField(max_length=2, choices=Nationality_CHOICES)


    Your_language_Preference= models.CharField(max_length=30, blank=True)
    your_photo= models.ImageField(max_length=15, blank=True)
    Upload_new_photo= models.ImageField(upload_to='profile_photo', blank=True)
    your_vision= models.CharField(max_length=500, blank=True)

  
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class password(models.Model):
    password= models.CharField(max_length=200)
    Your_new_Password= models.CharField(min_length=8, max_length=200)
    Confirm_new_Password= models.CharField(min_length=8, max_length=200)


    def __str__(self):
        return self.password_id




class Device(models.Model):
    Your_Phone_ID= models.CharField(max_length=100, blank=True,)
    Your_Phone_Brand= models.CharField(max_length=100, blank=True,)
    Phone_laptop_Brand= models.CharField(max_length=100, blank=True,)
    Your_Tablet_Brand= models.CharField(max_length=100, blank=True,)

    def __str__(self):
        return self.device_id




class Personal_ID(models.Model):
    Voice_ID= models.FileField(upload_to='voice_ids/')
    Face_ID= models.ImageField(upload_to='face_ids/')
    Biometrics_ID= models.BinaryField()
    video_ID= models.FileField(upload_to='video_ids/')
    ID_card= models.FileField(uplaod_to='ids/')

    # created= models.DateTimeField(auto_now_add=True)
    # upload= models.DateTimeField(auto_now=True)



class References(models.Model):
    Linkedin_profile= models.URLField()
    facebook_profile= models.URLField()
    Instagram_profile= models.URLField()
    Twitter_profile= models.URLField()
    Discord_profile= models.URLField()
    Tiktok_profile= models.URLField()
    Snapchat_profile= models.URLField()
    Pinterest_profile= models.URLField()
    Youtube_profile= models.URLField()
    Whatsapp_profile= models.URLField()
    Tumbir_profile= models.URLField()
    Xing_profile= models.URLField()
    Reddit_profile= models.URLField()
    Academia_profile= models.URLField()
    Personal_Reference_1= models.CharFi8eld(max_length=150)
    Personal_Reference_2= models.CharField(max_length=150)
    Personal_Reference_3= models.CharField(max_length=150)
    Personal_Reference_4= models.CharField(max_length=150)
    Personal_Reference_5= models.CharField(max_length=150)
    
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)



class Phone_number_verification(models.Model):
    STATUS_CHOICE= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choices=STATUS_CHOICE, default='Not Started')



class Email_verification(models.Model):
    STATUS_CHOICE= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choices= STATUS_CHOICE, default='not started')


    Voice_ID_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Voice_ID_verification)

    Face_ID_verification= [
        # CHIOCE_CHOICES
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Face_ID_verification)

    Biometric_ID_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Biometric_ID_verification)

    Voice_ID_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Voice_ID_verification)

    ID_Card_1_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=ID_Card_1_verification)

    ID_Card_2_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=ID_Card_2_verification)

    ID_Card_3_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=ID_Card_3_verification)

    ID_Card_4_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=ID_Card_4_verification)

    ID_Card_5_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=ID_Card_5_verification)

    ID_Card_1_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=ID_Card_1_verification)

    Signature_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Signature_verification)

    Socialmedia_profile_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Socialmedia_profile_verification)

    Personal_reference_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Personal_reference_verification)

    Personal_verification_by_witness= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Personal_verification_by_witness)

    Organization_verification= [
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=4, choice=Organization_verification)



    
class Email_verification(models.Model):
    STATUS_CHOICES= (
        ('Started', 'Not started'),
        ('Progress', 'In progress'),
        ('Accepted', 'Accepted after verification'),
        ('Rejected', 'Rejected after verifcation'),
    )
    email= models.EmailField()
    status= models.CharField(max_length=10, choices= STATUS_CHOICES, default='not started')




class Voiceverification(models.Model):
    STATUS_CHOICES= [
    ('started', 'Not started'),
    ('progress', 'In progress'),
    ('accepted', 'Accepted after verification'),
    ('rejected', 'Rejected after verifcation'),
    ]
    status= models.CharField(max_length=10, choices=STATUS_CHOICES, default='not started')




class Organisation(models.Model):
    Your_Organisation_Name= models.CharField(max_length=50, blank=True)
    Organisation_Address= models.CharField(max_length=100, blank=True)
    Zip_code= models.CharField(max_length=20, blank=True)

    City_Organisation_CHOICES= [
        ('City 1', 'City 1'),
        ('City 2', 'City 2'),
    ]
    models.CharField(max_length=2, choices=City_Organisation_CHOICES )

    Country_Organisation_CHOICES= [
        ('Country 1', 'Country 1'),
        ('Country 2', 'Country 2'),
    ]
    models.CharField(max_length=2, choices=Country_Organisation_CHOICES )

    Organisation_logo= models.CharField(max_length=150, blank=True)
    Upload_new_photo= models.ImageField(upload_to='profile_photo', blank=True)
    Latitude_of_0rganisaton= models.CharField(max_length=100, blank=True)
    Longitude_of_0rganisaton= models.CharField(max_length=100, blank=True)




class Geographic_profile(models.Model):
    Country_residing_CHOICES=[
        ('Country 1', 'Country 1'),
        ('Country 2', 'Country 2'),
    ]
    Country_residing= models.CharField(max_length=2, choices=Country_residing_CHOICES)

    City_residing= models.CharField(max_length=50, blank=True)
    Latitude_of_your_house= models.CharField(max_length=50, blank=True)
    Longitude_of_your_house= models.CharField(max_length=50, blank=True)

    Region_CHOICES=[
        ('North', 'North'),
        ('South', 'North'),
        ('East', 'East'),
        ('West', 'West'),
        ('South', 'South'),
    ]
    Region_inside_location= models.CharField(max_length=5, choices=Region_CHOICES)

    others= models.CharField(max_length=500, blank=True)





class Demographic_profile(models.Model):
    INCOME_CLASS_CHOICES=[
        ('T10', 'Top 10%'),
        ('T11_20' 'Top 11_20%'),
        ('T20_30' 'Top 20_30%'),
        ('T30_40' 'Top 30_40%'),
        ('T40_50' 'Top 40_50%'),
        ('B50%' 'Below 50%'),
    ]
    Income_class= models.CharField(max_length=6, choices=INCOME_CLASS_CHOICES)

    Your_Date_of_Birth= models.DateField()


    GENDER_CHOICES= [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    Gender= models.CharField(max_length=3, choices=GENDER_CHOICES)


    PARENTAL_STATUS_CHOICES= [
        ('P', 'Parent'),
        ('NP', 'Not_a_parent'),
    ]
    Parental_Status= models.CharField(max_length=2, choices=PARENTAL_STATUS_CHOICES)
 
    Your_Education= models.CharField(max_length=100, blank=True)
    Your_Occupation= models.CharField(max_length=100, blank=True)
    Your_family_size= models.CharField(max_length=100, blank=True)
    Others= models.CharField(max_length=100, blank=True)




class Psychographic_Profile(models.Model):
    Life_Style_CHOICES= [
        ('M', 'Modern'),
        ('T', 'Tradition'),
        ('T', 'Trandsetter'),
    ]
    Your_Life_Style= models.CharField(max_length=3, choices=Life_Style_CHOICES)


    IQ_Level_CHOICES= [
        ('A140', 'Above 140- "Near" genius or genius'),
        ('120-140', 'Very superior intelligence'),
        ('110-120', 'Superior intelligence'),
        ('90-110', 'Normal, or average, intelligence'),
        ('B90', 'Below average'),
    ] 
    Your_IQ_level= models.CharField(max_length=5, choices=IQ_Level_CHOICES)   


    Your_Attitude_CHOICES= [
        ('I', 'Innovators'),
        ('EA', 'Early Adopters'),
        ('EM', 'Early Majority'),
        ('LM', 'Late Majority'),
        ('L', 'Laggards'),
    ]
    Your_Attitude=models.CharField(max_length=5, choices=Your_Attitude_CHOICES)


    YOUR_Personality_CHOICES=[
        ('A', 'Architect'),
        ('L', 'Logician'),
        ('C', 'Commander'),
        ('ADVO', 'Advocate'),
        ('M', 'Mediator'),
        ('P', 'Protagonist'),
        ('CA', 'Campaigner'),
        ('LO', 'Logistician'),
        ('D', 'Defender'),
        ('EX', 'Executive'),
        ('CO', 'Consul'),
        ('V', 'Virtuoso'),
        ('AD', 'Adventurer'),
        ('E', 'Enterpernuer'),
        ('EN', 'Entertainer'),
    ]
    Your_Personality=models.CharField(max_length=15, choices=YOUR_Personality_CHOICES)

    Others= models.CharField(max_length=500, blank=True)

 
# correcction here
class Behavoiural_Profile(models.Model): 
    Benefits_CHOICES=[
        ('C', 'Convenience'),
        ('LL', 'Long Lasting'),
        ('E', 'Economy'),
        ('Vfm', 'Value for money'),
        ('M', 'Mobility'),
    ]
    Benefits_you_are_looking_for_while_buying_any_product_or_services= models.CharField(max_length=5, choices=Benefits_CHOICES)


    Role_CHOICES=[
        ('Initiator', 'Initiator'),
        ('Influencer', 'Influencer'),
        ('Decider', 'Decider'),
        ('Gatekepper', 'Gatkepper'),
        ('Buyer', 'Buyer'),
        ('User', 'User'),
    ]
    Your_role_while_buying_any_product_or_services= models.CharField(max_length=6, choices=Role_CHOICES)


    Brand_CHOICES=[
        (1, '1(Low'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5(high)'),
    ]
    Brand_loyality_level_you_will_consider_while_buying_any_product_or_services= models.CharField(max_length=5, choices=Brand_CHOICES)

    Others=models.CharField(max_length=200, blank=True)


class Usage_Profile(models.Model):
    Usage_CHOICES=[
        ('Heavy', 'Heavy'),
        ('Medium', 'Medium'),
        ('Light', 'Light'),
    ]
    Usage_rate_for_your_favorite_product_or_services= models.CharField(max_length=3, choices=Usage_CHOICES)


    Awearness_CHOICES=[
        ('Unawear', 'Unawear'),
        ('Awear', 'Awear'),
        ('Interested', 'Interested'),
        ('Enthusiastic', 'Enthusiastic')
    ]
    Awearness_level_while_using_the_product_or_services= models.CharField(max_length=4, choices=Awearness_CHOICES)

    Purpose_CHOICES=[
        ('Home', 'Home'),
        ('Work', 'Work'),
        ('Leisure', 'Lesisure'),
        ('Personal', 'Personal'),
        ('Gift', 'Gift'),
    ]
    Purpose_while_using_the_product_or_service= models.CharField(max_length=5, choices=Purpose_CHOICES)


    Other=models.CharField(max_length=200, blank=True) 
