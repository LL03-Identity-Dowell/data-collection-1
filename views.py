from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .forms import DeviceForm
from .forms import VoiceIDForm, FaceIDForm, BiometricIDForm, VideoIDForm, IDCard1Form, IDCard2Form, IDCard3Form, IDCard4Form, IDCard5Form, SignatureForm
from .forms import PersonalPreferencesForm
from .forms import VerificationStatusForm
from .models import VerificationStatus
from .forms import GeographicalProfileForm
from .forms import DemographicProfileForm
from .forms import PsychographicProfileForm
from .forms import BehavioralProfileForm
from .forms import UsageProfileForm


# Create your views here.
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/password_change_done/')
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})




def collect_device_information(request):
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = DeviceForm()
    return render(request, "collect_device_information.html", {"form": form})


def collect_voice_id(request):
    if request.method == 'POST':
        form = VoiceIDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_face_id')
    else:
        form = VoiceIDForm()
    return render(request, 'collect_voice_id.html', {'form': form})

def collect_face_id(request):
    if request.method == 'POST':
        form = FaceIDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_biometric_id')
    else:
        form = FaceIDForm()
    return render(request, 'collect_face_id.html', {'form': form})

def collect_biometric_id(request):
    if request.method == 'POST':
        form = BiometricIDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_video_id')
    else:
        form = BiometricIDForm()
    return render(request, 'collect_biometric_id.html', {'form': form})

def collect_video_id(request):
    if request.method == 'POST':
        form = VideoIDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_id_card_1')
    else:
        form = VideoIDForm()
    return render(request, 'collect_video_id.html', {'form': form})

def collect_id_card_1(request):
    if request.method == 'POST':
        form = IDCard1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_id_card_2')
    else:
        form = IDCard1Form()
    return render(request, 'collect_id_card_1.html', {'form': form})

def collect_id_card_2(request):
    if request.method == 'POST':
        form = IDCard2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_id_card_2')
    else:
        form = IDCard2Form()
    return render(request, 'collect_id_card_2.html', {'form': form})

def collect_id_card_3(request):
    if request.method == 'POST':
        form = IDCard3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collect_id_card_3')
    else:
        form =IDCard3Form()
    return render(request, 'collect_id_card_3.html', {'form': form})

def collect_id_card_4(request):
    if request.method == 'POST':
        form =IDCard4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save
            return redirect('collect_id_card_4')
    else:
        form =IDCard4Form()
    return render(request, 'collect_id_card_4.html', {'form': form})

def collect_id_card_5(request):
    if request.method =='POST':
        form =IDCard5Form(request.POST, request.FILES)
        if form.is_valid():
            form.save
            return redirect('collect_id_card_5.html', {'form': form})

def signature(request):
    if request.method =='POST':
        form =SignatureForm(request.POST)
        if form.is_vaild():
            form.save
            return redirect('signature.html', {'form': form})



def personal_preferences_view(request):
    if request.method == 'POST':
        form = PersonalPreferencesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonalPreferencesForm()
    return render(request, 'personal_preferences.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')




def verification_status_list(request):
    statuses = VerificationStatus.objects.all()
    return render(request, 'verification_status_list.html', {'statuses': statuses})

def create_verification_status(request):
    if request.method == 'POST':
        form = VerificationStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verification_status_list')
    else:
        form = VerificationStatusForm()
    return render(request, 'create_verification_status.html', {'form': form})

def update_verification_status(request, pk):
    status = VerificationStatus.objects.get(pk=pk)
    if request.method == 'POST':
        form = VerificationStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('verification_status_list')
    else:
        form = VerificationStatusForm(instance=status)
    return render(request, 'update_verification_status.html', {'form': form})

def delete_verification_status(request, pk):
    VerificationStatus.objects.get(pk=pk).delete()
    return redirect('verification_status_list')



def create_geographical_profile(request):
    if request.method == 'POST':
        form = GeographicalProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('geographical_profile_created')
    else:
        form = GeographicalProfileForm()
    return render(request, 'create_geographical_profile.html', {'form': form})



def demo_profile_create(request):
    if request.method == 'POST':
        form = DemographicProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DemographicProfileForm()
    return render(request, 'demo_profile_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')



def psychographic_profile(request):
    if request.method == 'POST':
        form = PsychographicProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PsychographicProfileForm()
    return render(request, 'psychographic_profile.html', {'form': form})

def success(request):
    return render(request, 'success.html')



def behavioral_profile(request):
    if request.method == 'POST':
        form = BehavioralProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BehavioralProfileForm()
    return render(request, 'behavioral_profile.html', {'form': form})
    


def usage_profile(request):
    if request.method == 'POST':
        form = UsageProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usage_profile_thanks')
    else:
        form = UsageProfileForm()
    return render(request, 'usage_profile.html', {'form': form})

def usage_profile_thanks(request):
    return render(request, 'usage_profile_thanks.html')

