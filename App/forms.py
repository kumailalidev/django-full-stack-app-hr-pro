from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


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

    # First name
    firstname = forms.CharField(
        label="First name",
        min_length=3,
        max_length=50,
        # required=False,
        error_messages={
            "required": "First name cannot be empty.",
        },
        validators=[
            RegexValidator(
                r"^[a-zA-ZÀ-ÿ\s]*$",
                message="Only letters is allowed !",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "style": "font-size: 13px; text-transform: capitalize;",
            }
        ),
    )

    # Last name
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
                "style": "font-size: 13px; text-transform: capitalize;",
            }
        ),
    )

    # Job code; always in uppercase
    job = Uppercase(
        label="Job code",
        min_length=5,
        max_length=5,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Example: FR-22",
                "style": "font-size: 13px; text-transform: uppercase;",
                "data-mask": "AA-00",
            }
        ),
    )

    # Email; always in lowercase
    email = Lowercase(
        label="Email address",
        min_length=8,
        max_length=50,
        # required=False,
        error_messages={
            "required": "Email field cannot be empty.",
        },
        validators=[
            RegexValidator(
                r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$",
                message="Put a valid email address !",
            )
        ],
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "style": "font-size: 13px; text-transform: lowercase;",
                # "autocomplete": "off",
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
    # age = forms.CharField(
    #     label="Your age",
    #     min_length=2,
    #     max_length=2,
    #     error_messages={
    #         "required": "Age field cannot be empty.",
    #     },
    #     validators=[
    #         RegexValidator(
    #             r"^[0-9]*$",
    #             message="Only number is allowed",
    #         )
    #     ],
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Age",
    #             "style": "font-size: 13px;",
    #             # "autocomplete": "off",
    #         }
    #     ),
    # )

    # Experience
    experience = forms.BooleanField(
        label="I have experience",
        required=False,
    )

    # Message
    message = forms.CharField(
        label="About you",
        min_length=50,
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Talk a little about you",
                "rows": 4,
                "style": "font-size: 13px;",
            }
        ),
    )

    # File
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={
                "style": "font-size: 13px;",
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
        # Labels Control
        # labels = {
        #     "gender": "Your Gender",
        #     "smoker": "Do you smoke ?",
        # }

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
            # Birthday
            "birth": forms.DateInput(
                attrs={
                    "style": "font-size: 13px; cursor: pointer;",
                    "type": "date",
                    # Block typing inside the input
                    "onkeydown": "return false",
                    "min": "1950-01-01",
                    "max": "2030-01-01",
                }
            ),
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
                    "style": "font-size: 13px;",
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
            # Personality
            "personality": forms.Select(
                attrs={
                    "style": "font-size: 13px;",
                }
            ),
        }

    # SUPER FUNCTION
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # ========== CONTROL PANEL (Individual Inputs) ==========

        # 1) INPUT REQUIRED
        # self.fields["message"].required = True

        # 2) INPUT DISABLED
        # self.fields["experience"].disabled = False

        # 3) INPUT READONLY
        # self.fields["email"].widget.attrs.update(
        #     {
        #         "readonly": "readonly",
        #     }
        # )

        # 4) SELECT OPTION
        # self.fields["personality"].choices = [
        #     ("", "Select a personality"),
        # ] + list(
        #     self.fields["personality"].choices
        # )[1:]

        # 5) WIDGETS (Inside/Outside)
        """
        Overrides all the other widget values
        """
        # self.fields["phone"].widget.attrs.update(
        #     {
        #         "style": "font-size: 18px;",
        #         "placeholder": "No Phone",
        #         "data-mask": "(00) 00-00",
        #     }
        # )

        # 6) ERROR MESSAGES
        """
        Overrides all the other default error messages
        """
        # self.fields["firstname"].error_messages.update(
        #     {
        #         "required": "This is super function overridden error message",
        #     }
        # )

        # ========== ADVANCED CONTROL PANEL (Multiple Inputs) ==========
        # 1) READONLY
        # readonly = ["firstname", "lastname", "job", "email", "age", "phone", "message"]
        # for field in readonly:
        #     self.fields[field].widget.attrs["readonly"] = "true"

        # 2) DISABLED
        # disabled = ["personality", "salary", "gender", "smoker", "experience"]
        # for field in disabled:
        #     self.fields[field].widget.attrs["disabled"] = "true"

        # 3) ERROR MESSAGES
        # error_messages = [
        #     "firstname",
        #     "lastname",
        #     "job",
        #     "email",
        #     "age",
        #     "phone",
        #     "personality",
        #     "salary",
        #     "gender",
        #     "smoker",
        #     "file",
        # ]
        # for field in error_messages:
        #     self.fields[field].error_messages.update({"required": "Field required!"})

        # 4) FONT SIZE
        # font_size = [
        #     "firstname",
        #     "lastname",
        #     "job",
        #     "age",
        # ]
        # for field in font_size:
        #     self.fields[field].widget.attrs.update(
        #         {
        #             "style": "font-size: 18px;",
        #         }
        #     )

        # 5) AUTO COMPLETE = OFF (Input History)
        # NOTE: This also control fields inside admin panel, therefore auto_complete fields inside
        #       admin panel should NOT be readonly
        # auto_complete = [
        #     "firstname",
        #     "lastname",
        #     "email",
        #     "phone",
        # ]
        # for field in auto_complete:
        #     self.fields[field].widget.attrs.update(
        #         {
        #             "autocomplete": "off",
        #         }
        #     )

    # ______________________________________ END // SUPER FUNCTION ______________________________________

    # ====================================== FUNCTION (METHOD CLEAN) ======================================

    # 1) FUNCTION TO PREVENT DUPLICATE ENTRIES

    # Method 1 (loop for)
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError(
    #                 "Denied! " + email + "  is already registered."
    #             )
    #     return email

    # Method 2 (if statement w/ filter)
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Candidate.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Denied! {} is already registered.".format(email)
            )
        return email

    # 2) JOB CODE (Job Code Validation)
    def clean_job(self):
        job = self.cleaned_data.get("job")
        if job == "FR-22" or job == "BA-10" or job == "FU-15":
            return job
        else:
            raise forms.ValidationError("Denied! This code is invalid.")

    # 3) AGE (Range: 18 - 65)
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < "18" or age > "65":
            raise forms.ValidationError("Denied! Age must be between 18 and 65")
        # else:
        #     return age
        return age

    # 4) PHONE (Prevent incomplete values)
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone) != 15:
            raise forms.ValidationError("Phone field is incomplete")
        # else:
        #     return phone
        return phone
