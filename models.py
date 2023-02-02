from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    pin_code = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    team_code = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='profiles/')
    vision = models.TextField()
    native_language = models.CharField(
        max_length=10,
        choices=(
            ('english', 'English'),
            ('chinese', 'Chinese')
        )
    )
    nationality = models.CharField(
        max_length=10,
        choices=(
            ('english', 'English'),
            ('chinese', 'Chinese')
        )
    )
    Your_Language_Preferences = models.CharField(
        max_length=10,
        choices=(
            ('english', 'English'),
            ('chinese', 'Chinese')
        )
    )

class PasswordChangeForm(models.Model):
    current_password = models.CharField(max_length=255)
    new_password = models.CharField(max_length=255)
    confirm_new_password = models.CharField(max_length=255)


class Device(models.Model):
    phone_id = models.CharField(max_length=100)
    phone_brand = models.CharField(max_length=100)
    phone_model = models.CharField(max_length=100)
    laptop_brand = models.CharField(max_length=100)
    laptop_model = models.CharField(max_length=100)
    tablet_brand = models.CharField(max_length=100)
    tablet_model = models.CharField(max_length=100)



class VoiceID(models.Model):
    voice = models.FileField(upload_to='voice_id/')

class FaceID(models.Model):
    face = models.FileField(upload_to='face_id/')

class BiometricID(models.Model):
    biometric = models.FileField(upload_to='biometric_id/')

class VideoID(models.Model):
    video = models.FileField(upload_to='video_id/')

class IDCard1(models.Model):
    id_card_1 = models.FileField(upload_to='id_card_1/')

class IDCard2(models.Model):
    id_card_2 = models.FileField(upload_to='id_card_2/')

class IDCard3(models.Model):
    id_card_3 = models.FileField(upload_to='id_card_3/')

class IDCard4(models.Model):
    id_card_4 = models.FileField(upload_to='id_card_4/')

class IDCard5(models.Model):
    id_card_5 = models.FileField(upload_to='id_card_5/')

class Signature(models.Model):
    signature = models.FileField(upload_to='signature/')



class PersonalPreferences(models.Model):
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    snapchat = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    tumblr = models.URLField(blank=True, null=True)
    xing = models.URLField(blank=True, null=True)
    reddit = models.URLField(blank=True, null=True)
    academia = models.URLField(blank=True, null=True)
    personal_reference_1 = models.TextField(blank=True, null=True)
    personal_reference_2 = models.TextField(blank=True, null=True)
    personal_reference_3 = models.TextField(blank=True, null=True)
    personal_reference_4 = models.TextField(blank=True, null=True)
    personal_reference_5 = models.TextField(blank=True, null=True)



class PhoneNumberVerification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class EmailVerification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class Voice_ID_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Face_ID_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Biometric_ID_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Video_ID_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class ID_Card_1_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class ID_Card_2_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class ID_Card_3_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class ID_Card_4_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class ID_Card_5_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Signature_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Social_media_profile_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Personal_reference_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Personal_Verification_by_witness(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


class Organisation_Verification(models.Model):
    STATUS_CHOICES = (
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('accepted', 'Accepted after Verification'),
        ('rejected', 'Rejected after Verification')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)



class GeographicalProfile(models.Model):
    COUNTRY_CHOICES = [
        ('country1', 'Country 1'),
        ('country2', 'Country 2'),
    ]
    REGION_CHOICES = [
        ('north', 'North'),
        ('east', 'East'),
        ('west', 'West'),
        ('center', 'Center'),
    ]
    
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    others = models.TextField()



class DemographicProfile(models.Model):
    INCOME_CLASS_CHOICES = [
        ('top_10', 'Top 10%'),
        ('top_11_20', 'Top 11-20'),
        ('top_20_30', 'Top 20-30%'),
        ('top_30_40', 'Top 30-40%'),
        ('top_40_50', 'Top 40-50%'),
        ('below_50', 'Below 50%'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    PARENTAL_STATUS_CHOICES = [
        ('parent', 'Parent'),
        ('not_parent', 'Not a parent'),
    ]
    
    income_class = models.CharField(max_length=20, choices=INCOME_CLASS_CHOICES)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    parental_status = models.CharField(max_length=20, choices=PARENTAL_STATUS_CHOICES)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    family_size = models.PositiveSmallIntegerField()
    others = models.TextField()



class PsychographicProfile(models.Model):
    LIFE_STYLE_CHOICES = [
        ('modern', 'Modern'),
        ('traditional', 'Traditional'),
        ('trendsetter', 'Trendsetter'),
    ]

    IQ_LEVEL_CHOICES = [
        ('above_140', 'Above 140 - "Near" genius or genius'),
        ('120_140', '120-140 - very superior intelligence'),
        ('110_120', '110-120 - Superior intelligence'),
        ('90_110', '90-110 - Normal, or average, intelligence'),
        ('below_90', 'Below 90 - Below average'),
    ]

    ATTITUDE_CHOICES = [
        ('innovators', 'Innovators'),
        ('early_adapters', 'Early Adapters'),
        ('early_majority', 'Early Majority'),
        ('late_majority', 'Late Majority'),
        ('laggards', 'Laggards'),
    ]

    PERSONALITY_CHOICES = [
        ('architect', 'Architect'),
        ('logician', 'Logician'),
        ('commander', 'Commander'),
        ('debater', 'Debater'),
        ('advocate', 'Advocate'),
        ('mediator', 'Mediator'),
        ('protagonist', 'Protagonist'),
        ('campaigner', 'Campaigner'),
        ('logistician', 'Logistician'),
        ('defender', 'Defender'),
        ('executive', 'Executive'),
        ('consul', 'Consul'),
        ('virtuoso', 'Virtuoso'),
        ('adventurer', 'Adventurer'),
        ('entrepreneur', 'Entrepreneur'),
        ('entertainer', 'Entertainer'),
        ('others', 'Others'),
    ]

    life_style = models.CharField(max_length=20, choices=LIFE_STYLE_CHOICES)
    iq_level = models.CharField(max_length=20, choices=IQ_LEVEL_CHOICES)
    attitude = models.CharField(max_length=20, choices=ATTITUDE_CHOICES)
    personality = models.CharField(max_length=20, choices=PERSONALITY_CHOICES)


class BehavioralProfile(models.Model):
    BENEFIT_CHOICES = [
        ('convenience', 'Convenience'),
        ('lasting', 'Long lasting'),
        ('economy', 'Economy'),
        ('value', 'Value of money'),
        ('mobility', 'Mobility')
    ]

    ROLE_CHOICES = [
        ('initiator', 'Initiator'),
        ('influencer', 'Influencer'),
        ('decider', 'Decider'),
        ('gatekeeper', 'Gatekeeper'),
        ('buyer', 'Buyer'),
        ('user', 'User')
    ]

    LOYALTY_CHOICES = [
        (1, '1 (Low)'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 (High)')
    ]

    benefit = models.CharField(
        max_length=20,
        choices=BENEFIT_CHOICES,
        default='convenience'
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='initiator'
    )
    loyalty = models.PositiveSmallIntegerField(
        choices=LOYALTY_CHOICES,
        default=1
    )
    others = models.TextField(blank=True)



class UsageProfile(models.Model):
    USAGE_RATE_CHOICES = [
        ('HEAVY', 'Heavy'),
        ('MEDIUM', 'Medium'),
        ('LIGHT', 'Light'),
    ]
    usage_rate = models.CharField(
        max_length=7,
        choices=USAGE_RATE_CHOICES,
        default='HEAVY',
    )

    AWARENESS_LEVEL_CHOICES = [
        ('UNAWARE', 'Unaware'),
        ('AWARE', 'Aware'),
        ('INTERESTED', 'Interested'),
        ('ENTHUSIASTIC', 'Enthusiastic'),
    ]
    awareness_level = models.CharField(
        max_length=12,
        choices=AWARENESS_LEVEL_CHOICES,
        default='UNAWARE',
    )

    PURPOSE_CHOICES = [
        ('HOME', 'Home'),
        ('WORK', 'Work'),
        ('LEISURE', 'Leisure'),
        ('PERSONAL', 'Personal'),
        ('GIFT', 'Gift'),
        ('OTHER', 'Other'),
    ]
    purpose = models.CharField(
        max_length=8,
        choices=PURPOSE_CHOICES,
        default='HOME',
    )




