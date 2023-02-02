from django import forms
from .models import Profile
from django import forms
from .models import PasswordChangeForm
from .models import Device
from .models import VoiceID, FaceID, BiometricID, VideoID, IDCard1, IDCard2, IDCard3, IDCard4, IDCard5, Signature
from .models import PersonalPreferences
from .models import PhoneNumberVerification
from .models import GeographicalProfile
from .models import DemographicProfile
from .models import BehavioralProfile
from .models import UsageProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'pin_code',
            'city',
            'country',
            'designation',
            'team_code',
            'photo',
            'vision'
        ]

class PasswordChangeFormForm(forms.ModelForm):
    class Meta:
        model = PasswordChangeForm
        fields = ['current_password', 'new_password', 'confirm_new_password']
        widgets = {
            'current_password': forms.PasswordInput(),
            'new_password': forms.PasswordInput(),
            'confirm_new_password': forms.PasswordInput(),
        }



class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            "phone_id",
            "phone_brand",
            "phone_model",
            "laptop_brand",
            "laptop_model",
            "tablet_brand",
            "tablet_model",
        ]



class VoiceIDForm(forms.ModelForm):
    class Meta:
        model = VoiceID
        fields = ['voice']

class FaceIDForm(forms.ModelForm):
    class Meta:
        model = FaceID
        fields = ['face']

class BiometricIDForm(forms.ModelForm):
    class Meta:
        model = BiometricID
        fields = ['biometric']

class VideoIDForm(forms.ModelForm):
    class Meta:
        model = VideoID
        fields = ['video']

class IDCard1Form(forms.ModelForm):
    class Meta:
        model = IDCard1
        fields = ['id_card_1']

class IDCard2Form(forms.ModelForm):
    class Meta:
        model = IDCard2
        fields = ['id_card_2']

class IDCard3Form(forms.ModelForm):
    class Meta:
        model = IDCard3
        fields = ['id_card_3']

class IDCard4Form(forms.ModelForm):
    class Meta:
        model = IDCard4
        fields = ['id_card_4']

class IDCard5Form(forms.ModelForm):
    class Meta:
        model = IDCard5
        fields = ['id_card_5']

class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['signature']



class PersonalPreferencesForm(forms.ModelForm):
    class Meta:
        model = PersonalPreferences
        fields = [
            'linkedin', 'facebook', 'instagram', 'twitter', 'discord',
            'tiktok', 'snapchat', 'pinterest', 'youtube', 'whatsapp',
            'tumblr', 'xing', 'reddit', 'academia',
            'personal_reference_1', 'personal_reference_2', 'personal_reference_3',
            'personal_reference_4', 'personal_reference_5'
        ]


class PhoneNumberVerificationForm(forms.ModelForm):
    class Meta:
        model = PhoneNumberVerification
        fields = ['status']


class GeographicalProfileForm(forms.ModelForm):
    class Meta:
        model = GeographicalProfile
        fields = ['country', 'city', 'latitude', 'longitude', 'region', 'others']



class DemographicProfileForm(forms.ModelForm):
    class Meta:
        model = DemographicProfile
        fields = '__all__'



class PsychographicProfileForm(forms.Form):
    LIFE_STYLE_CHOICES = [        ('modern', 'Modern'),        ('traditional', 'Traditional'),        ('trendsetter', 'Trendsetter'),    ]

    IQ_LEVEL_CHOICES = [        ('above_140', 'Above 140 - "Near" genius or genius'),        ('120_140', '120-140 - very superior intelligence'),        ('110_120', '110-120 - Superior intelligence'),        ('90_110', '90-110 - Normal, or average, intelligence'),        ('below_90', 'Below 90 - Below average'),    ]

    ATTITUDE_CHOICES = [        ('innovators', 'Innovators'),        ('early_adapters', 'Early Adapters'),        ('early_majority', 'Early Majority'),        ('late_majority', 'Late Majority'),        ('laggards', 'Laggards'),    ]

    PERSONALITY_CHOICES = [        ('architect', 'Architect'),        ('logician', 'Logician'),        ('commander', 'Commander'),        ('debater', 'Debater'),        ('advocate', 'Advocate'),        ('mediator', 'Mediator'),        ('protagonist', 'Protagonist'),        ('campaigner', 'Campaigner'),        ('logistician', 'Logistician'),        ('defender', 'Defender'),        ('executive', 'Executive'),        ('consul', 'Consul'),        ('virtuoso', 'Virtuoso'),        ('adventurer', 'Adventurer'),        ('entrepreneur', 'Entrepreneur'),        ('entertainer', 'Entertainer'),        ('others', 'Others'),    ]

    life_style = forms.ChoiceField(choices=LIFE_STYLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    iq_level = forms.ChoiceField(choices=IQ_LEVEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    attitude = forms.ChoiceField(choices=ATTITUDE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    personality = forms.ChoiceField(choices=PERSONALITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))



class BehavioralProfileForm(forms.ModelForm):
    class Meta:
        model = BehavioralProfile
        fields = ['benefit', 'role', 'loyalty', 'others']
        widgets = {
            'benefit': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'loyalty': forms.Select(attrs={'class': 'form-control'}),
            'others': forms.Textarea(attrs={'class': 'form-control'})
        }


class UsageProfileForm(forms.ModelForm):
    class Meta:
        model = UsageProfile
        fields = ['usage_rate', 'awareness_level', 'purpose']
