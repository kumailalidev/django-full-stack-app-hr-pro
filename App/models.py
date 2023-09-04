from django.db import models

SITUATION = (
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Disapproved", "Disapproved"),
)


class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
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
