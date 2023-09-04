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
            RegexValidator(
                r"^[a-zA-ZÀ-ÿ\s]*$",
                message="Only letters is allowed !",
            )
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
            RegexValidator(
                r"^[a-zA-ZÀ-ÿ\s]*$",
                message="Only letters is allowed !",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
            }
        ),
    )
    job = forms.CharField(
        label="Job code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Example: FR-22",
            }
        ),
    )
    email = forms.CharField(
        label="Email address",
        min_length=8,
        max_length=50,
        # required=False,
        validators=[
            RegexValidator(
                r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                message="Put a valid email address !",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
            }
        ),
    )
    # Validating age
    # Method 1 (Using type attribute)
    # age = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "type": "number",
    #         }
    #     )
    # )

    # Method 02 (Using Regex)
    age = forms.CharField(
        label="Your age",
        min_length=2,
        max_length=2,
        validators=[
            RegexValidator(
                r"^[0-9]*$",
                message="Only number is allowed",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Age",
            }
        ),
    )

    message = forms.CharField(
        label="About you",
        min_length=50,
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Talk a little about you",
                "rows": 10,
            }
        ),
    )

    class Meta:
        model = Candidate
        fields = "__all__"
        # fields = ["firstname", "lastname", "email", "age", "message",]
        # exclude = ["firstname", "lastname", "email", "age", "message",]

        # Outside Widget
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "style": "font-size: 13px;",
                    "placeholder": "Phone",
                    "data-mask": "(00) 00000-0000",
                }
            )
        }
