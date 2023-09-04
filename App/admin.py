from django.contrib import admin
from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ["firstname", "lastname", "email", "job"]
    search_fields = ["firstname", "lastname", "email"]
    list_per_page = 10


admin.site.register(Candidate, CandidateAdmin)
