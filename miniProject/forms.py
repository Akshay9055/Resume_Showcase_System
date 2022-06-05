from django import forms
from .models import Document, Profile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_uploads']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','bio','branch','image']
