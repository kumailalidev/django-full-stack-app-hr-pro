from django.db import models

SITUATION = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Disapproved", "Disapproved"),
)

PERSONALITY = (
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
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(
        max_length=50, null=True, choices=SITUATION, default="Pending"
    )

    # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    def __str__(self):
        return self.firstname
