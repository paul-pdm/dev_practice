from django import forms
from patient_first.models import Patient,Encounter,UserProfile
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class PatientForm(forms.ModelForm):
    name = forms.CharField(max_length=20, help_text ="First Name")
    #date_of_birth = forms.DateField(required=True, help_text="Date of Birth MM/DD/YYYY")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Patient
        fields = ('name', )


class EncounterForm(forms.ModelForm):
    note_type= forms.CharField(max_length=20, help_text="Note Type")
    note = forms.CharField(widget=forms.Textarea, help_text="Enter Note")
    signature = forms.CharField(max_length=40, help_text="eSignature")


    class Meta:
        model = Encounter
        fields = ('note_type', 'note', 'signature', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields= ('website', 'picture')

