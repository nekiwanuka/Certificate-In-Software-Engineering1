from django import forms
from .models import KYC


class KYCRegistrationForm(forms.ModelForm):
    class Meta:
        model = KYC
        fields = [
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "country",
            "state_or_district",
            "town",
            "zip_code",
            "phone_number_one",
            "phone_number_two",
            "email",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }
