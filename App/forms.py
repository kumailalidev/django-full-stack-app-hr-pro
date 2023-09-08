from django import forms
from .models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date  # Used in Birthdate
import datetime  # Used to prevent future dates


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
                "rows": 6,
                "style": "font-size: 13px;",
            }
        ),
    )

    # File (Resume upload)
    file = forms.FileField(
        label="Resume",
        # required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "style": "font-size: 13px;",
                # Method # 01
                # "accept": "application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            }
        ),
    )

    # Image (Upload photo)
    image = forms.FileField(
        label="Photo",
        widget=forms.ClearableFileInput(
            attrs={
                "style": "font-size: 13px;",
                # Allowed extensions
                "accept": "image/png, image/jpeg",
            }
        ),
    )

    # Institution
    institution = forms.CharField(
        label="Institution",
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "style": "font-size: 13px;",
                "placeholder": "Institution name",
            }
        ),
    )

    # College course
    course = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "style": "font-size: 13px;",
                "placeholder": "Your college course",
            }
        ),
    )

    # About college course
    about_course = forms.CharField(
        label="About your college course",
        min_length=50,
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell us about your college course",
                "style": "font-size: 13px;",
                "rows": 7,
            }
        ),
    )

    # About the Job
    about_job = forms.CharField(
        label="About your last job",
        min_length=50,
        max_length=1000,
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell us a little about what you did at the company...",
                "style": "font-size: 13px;",
                "rows": 7,
            }
        ),
    )

    # Company
    company = forms.CharField(
        label="Last Company",
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Company name",
                "style": "font-size: 13px;",
            }
        ),
    )

    # Position
    position = forms.CharField(
        label="Last Company",
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your occupation",
                "style": "font-size: 13px;",
            }
        ),
    )

    employed = forms.BooleanField(label="I am employed", required=False)
    remote = forms.BooleanField(label="I agree to work remotely", required=False)
    travel = forms.BooleanField(label="I'm available for travel", required=False)

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

        labels = {
            "started_course": "Started",
            "finished_course": "Finished",
            "started_job": "Started",
            "finished_job": "Finished",
        }

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
            # Started course
            "started_course": forms.DateInput(
                attrs={
                    "style": "font-size: 13px; cursor: pointer;",
                    "type": "date",
                    # Block typing inside the input
                    "onkeydown": "return false",
                    "min": "1950-01-01",
                    "max": "2030-01-01",
                }
            ),
            # Finished Course
            "finished_course": forms.DateInput(
                attrs={
                    "style": "font-size: 13px; cursor: pointer;",
                    "type": "date",
                    # Block typing inside the input
                    "onkeydown": "return false",
                    "min": "1950-01-01",
                    "max": "2030-01-01",
                }
            ),
            # Started Job
            "started_job": forms.DateInput(
                attrs={
                    "style": "font-size: 13px; cursor: pointer;",
                    "type": "date",
                    # Block typing inside the input
                    "onkeydown": "return false",
                    "min": "1950-01-01",
                    "max": "2030-01-01",
                }
            ),
            # Finished Job
            "finished_job": forms.DateInput(
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
            # Course Status
            "status_course": forms.Select(
                attrs={
                    "style": "font-size: 13px;",
                }
            ),
        }

    # SUPER FUNCTION
    # Notes
    #     - Super function controls all the inputs inside frontend, backend and admin
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)

        # Disable inputs (By ID/PK)
        # instance = getattr(self, "instance", None)
        # if instance and instance.pk:
        #     self.fields["firstname"].disabled = True

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

        # 6) DISABLE ALL INPUTS (By ID/PK)
        # instance = getattr(self, "instance", None)
        # array = [
        #     "experience",
        #     "gender",
        #     "firstname",
        #     "lastname",
        #     "job",
        #     "email",
        #     "phone",
        #     "salary",
        #     "birth",
        #     "personality",
        #     "smoker",
        #     "file",
        #     "image",
        #     "frameworks",
        #     "languages",
        #     "databases",
        #     "libraries",
        #     "mobile",
        #     "others",
        #     "message",
        #     "status_course",
        #     "started_course",
        #     "finished_course",
        #     "course",
        #     "institution",
        #     "about_course",
        #     "started_job",
        #     "finished_job",
        #     "company",
        #     "position",
        #     "about_job",
        #     "employed",
        #     "remote",
        #     "travel",
        # ]
        # for field in array:
        #     if instance and instance.pk:
        #         self.fields[field].disabled = True
        #         self.fields['file'].widget.attrs.update({"style": "display: none;"})
        #         self.fields['image'].widget.attrs.update({"style": "display: none;"})

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
    # def clean_age(self):
    #     age = self.cleaned_data.get("age")
    #     if age < "18" or age > "65":
    #         raise forms.ValidationError("Denied! Age must be between 18 and 65")
    #     # else:
    #     #     return age
    #     return age

    # 4) PHONE (Prevent incomplete values)
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone) != 15:
            raise forms.ValidationError("Phone field is incomplete")
        # else:
        #     return phone
        return phone

    # 5) RESTRICTION (file extensions - Method 2 via function)
    # Method 2
    # def clean_file(self):
    #     file = self.cleaned_data["file"]
    #     content_type = file.content_type
    #     if content_type == "application/pdf" or content_type == "application/msword":
    #         return file
    #     else:
    #         raise forms.ValidationError("Only: PDF - DOC - DOCX")

    # Method 3
    def clean_file(self):
        # Get data
        file = self.cleaned_data.get("file", False)
        # Variables
        EXT = ["pdf", "doc", "docx"]
        ext = str(file).split(".")[-1]
        type = ext.lower()
        # Statement
        # a) Accept only pdf - doc - docx
        if type not in EXT:
            raise forms.ValidationError("Only: PDF - DOC - DOCX")
        # b) Prevent upload more than 2MB
        if file.size > 2 * 1048476:
            raise forms.ValidationError("Denied: Maximum allowed is 2mb")
        return file

    # Method 3 (When required is set to False)
    # def clean_file(self):
    #     # Get data
    #     file = self.cleaned_data.get("file", False)
    #     if file is not None:
    #         # Variables
    #         EXT = ["pdf", "doc", "docx"]
    #         ext = str(file).split(".")[-1]
    #         type = ext.lower()
    #         # Statement
    #         # a) Accept only pdf - doc - docx
    #         if type not in EXT:
    #             raise forms.ValidationError("Only: PDF - DOC - DOCX")
    #         # b) Prevent upload more than 2MB
    #         if file.size > 2 * 1048476:
    #             raise forms.ValidationError("Denied: Maximum allowed is 2mb")
    #         return file

    # 6) IMAGE (Maximum upload size = 2mb)
    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image.size > 2 * 1048476:
            raise forms.ValidationError("Denied: Maximum allowed is 2mb")
        return image

    # 7) BIRTHDAY (Rage: 18 and 65)
    def clean_birth(self):
        birth = self.cleaned_data.get("birth")
        # Variables
        b = birth
        now = date.today()
        age = (now.year - b.year) - ((now.month, now.day) < (b.month, b.day))
        print(age)
        # Statement
        if age < 18 or age > 65:
            raise forms.ValidationError("Denied: Age must be between 18 and 65")
        return birth

    # 8) Prevent FUTURES dates (card 3 and card 4)
    # A) College
    def clean_started_course(self):
        started_course = self.cleaned_data["started_course"]
        if started_course > datetime.date.today():
            raise forms.ValidationError("Future dates is invalid")
        return started_course

    def clean_finished_course(self):
        finished_course = self.cleaned_data["finished_course"]
        if finished_course > datetime.date.today():
            raise forms.ValidationError("Future dates is invalid")
        return finished_course

    # B) JOB
    def clean_started_job(self):
        started_job = self.cleaned_data["started_job"]
        if started_job > datetime.date.today():
            raise forms.ValidationError("Future dates is invalid")
        return started_job

    def clean_finished_job(self):
        finished_job = self.cleaned_data["finished_job"]
        if finished_job > datetime.date.today():
            raise forms.ValidationError("Future dates is invalid")
        return finished_job
