from django import forms
from .models import Candidate
from django.core.validators import RegexValidator


class CandidateForm(forms.ModelForm):
    # Validations
    firstname = forms.CharField(
        label="First name",
        min_length=3,
        max_length=50,
        # required=False,
        validators=[
            RegexValidator(r"^[a-zA-ZÀ-ÿ\s]*$", message="Only letters is allowed !")
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
            }
        ),
    )

    lastname = forms.CharField(
        label="Last name",
        min_length=3,
        max_length=50,
        # required=False,
        validators=[
            RegexValidator(r"^[a-zA-ZÀ-ÿ\s]*$", message="Only letters is allowed !")
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
            }
        ),
    )

    class Meta:
        model = Candidate
        fields = "__all__"
        # fields = ["firstname", "lastname", "email", "age", "message",]
        # exclude = ["firstname", "lastname", "email", "age", "message",]
