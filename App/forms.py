from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator


# Every letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()


# Every letters to lowercase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


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

    # Job code always in uppercase
    job = Uppercase(
        label="Job code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Example: FR-22",
            }
        ),
    )

    # email always in lowercase
    email = Lowercase(
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

    experience = forms.BooleanField(
        label="I have experience",
        required=False,
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

    # Method # 01 (Gender) (Outside the Meta class)
    # GENDER = [
    #     ("M", "Male"),
    #     ("F", "Female"),
    # ]
    # gender = forms.CharField(
    #     label="Gender",
    #     widget=forms.RadioSelect(choices=GENDER),
    # )

    class Meta:
        model = Candidate
        exclude = ["created_at", "situation"]
        # fields = "__all__"
        # fields = ["firstname", "lastname", "email", "age", "message",]

        # Native choice field
        SALARY = (
            ("", "Salary expectation (month)"),
            ("Between ($3000 and $4000)", "Between ($3000 and $4000)"),
            ("Between ($4000 and $5000)", "Between ($4000 and $5000)"),
            ("Between ($5000 and $7000)", "Between ($5000 and $7000)"),
            ("Between ($7000 and $10000)", "Between ($7000 and $10000)"),
        )
        GENDER = [
            ("M", "Male"),
            ("F", "Female"),
        ]

        # Outside Widgets
        widgets = {
            # Phone field
            "phone": forms.TextInput(
                attrs={
                    "style": "font-size: 13px;",
                    "placeholder": "Phone",
                    "data-mask": "(00) 00000-0000",
                }
            ),
            # Salary field
            "salary": forms.Select(
                choices=SALARY,
                attrs={
                    "class": "form-control",
                },  # Bootstrap inside the forms.py
            ),
            # Gender Choices
            # Method # 02 (Gender) (inside the Meta class)
            "gender": forms.RadioSelect(
                choices=GENDER,
                attrs={
                    "class": "btn-check",
                },
            ),
            # Smoker Choices
            "smoker": forms.RadioSelect(
                choices=SMOKER,
                attrs={
                    "class": "btn-check",
                },
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Optional method to control) ==========

        # ========== SELECT OPTION ==========
        self.fields["personality"].choices = [
            ("", "Select a personality"),
        ] + list(
            self.fields["personality"].choices
        )[1:]

        # ========== WIDGET CONTROL ==========
