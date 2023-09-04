from django.db import models


class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
