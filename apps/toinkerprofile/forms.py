from django import forms
from .models import ToinkerProfile

class OinkerProfileForm(forms.ModelForm):
	class Meta:
		model = ToinkerProfile
		fields = ('avatar',)