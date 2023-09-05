from django.db import models
from multiselectfield import MultiSelectField

SITUATION = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Disapproved", "Disapproved"),
)

PERSONALITY = (
    ("", "Select a personality"),
    ("I am outgoing", "I am outgoing"),
    ("I am sociable", "I am sociable"),
    ("I am antisocial", "I am antisocial"),
    ("I am discrete", "I am discrete"),
    ("I am serious", "I am serious"),
)

SMOKER = (
    ("1", "Yes"),
    ("2", "No"),
)

# Multiple Checkboxes
FRAMEWORKS = (
    ("Laravel", "Laravel"),
    ("Angular", "Angular"),
    ("Django", "Django"),
    ("Flask", "Flask"),
    ("Vue", "Vue"),
    ("Others", "Others"),
)
LANGUAGES = (
    ("Python", "Python"),
    ("Javascript", "Javascript"),
    ("Java", "Java"),
    ("C++", "C++"),
    ("Ruby", "Ruby"),
    ("Others", "Others"),
)
DATABASES = (
    ("MySql", "MySql"),
    ("Postgree", "Postgree"),
    ("MongoDB", "MongoDB"),
    ("Sqlite3", "Sqlite3"),
    ("Oracle", "Oracle"),
    ("Others", "Others"),
)
LIBRARIES = (
    ("Ajax", "Ajax"),
    ("Jquery", "Jquery"),
    ("React.js", "React.js"),
    ("Chart.js", "Chart.js"),
    ("Gsap", "Gsap"),
    ("Others", "Others"),
)
MOBILE = (
    ("React native", "React native"),
    ("Kivy", "Kivy"),
    ("Flutter", "Flutter"),
    ("Ionic", "Ionic"),
    ("Xamarim", "Xamarim"),
    ("Others", "Others"),
)
OTHERS = (
    ("UML", "UML"),
    ("SQL", "SQL"),
    ("Docker", "Docker"),
    ("GIT", "GIT"),
    ("GraphQL", "GraphQL"),
    ("Others", "Others"),
)


class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, choices=SMOKER, default="")
    email = models.EmailField(max_length=50)
    message = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(
        max_length=50, null=True, choices=SITUATION, default="Pending"
    )
    # Multiple Checkboxes
    frameworks = MultiSelectField(choices=FRAMEWORKS, default="")
    languages = MultiSelectField(choices=LANGUAGES, default="")
    databases = MultiSelectField(choices=DATABASES, default="")
    libraries = MultiSelectField(choices=LIBRARIES, default="")
    mobile = MultiSelectField(choices=MOBILE, default="")
    others = MultiSelectField(choices=OTHERS, default="")

    # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname
