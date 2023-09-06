from django.contrib import admin
from .models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html


class CandidateAdmin(admin.ModelAdmin):
    form = CandidateForm
    radio_fields = {"smoker": admin.HORIZONTAL}  # REDUNDANT
    list_filter = ["situation"]
    readonly_fields = [
        "firstname",
        "lastname",
        "job",
        "email",
        "age",
        "phone",
        "salary",
        "personality",
        "gender",
        "smoker",
        "experience",
        "file",
        "frameworks",
        "languages",
        "databases",
        "libraries",
        "mobile",
        "others",
        "message",
    ]
    exclude = ["status"]
    list_display = [
        "name",
        "job",
        "email",
        "age",
        "created_at",
        "status",
        "_",
    ]
    search_fields = [
        "firstname",
        "lastname",
        "email",
        "age",
        "situation",
    ]
    list_per_page = 10

    # Function to hide F-name and L-name (when clicking over the candidates)
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove("firstname")
            fields.remove("lastname")
        return fields

    # Function to change the icons
    def _(self, obj):
        if obj.situation == "Approved":
            return True
        elif obj.situation == "Pending":
            return None
        else:
            return False

    _.boolean = True

    # Function to color the text
    def status(self, obj):
        if obj.situation == "Approved":
            color = "#28a745"
        elif obj.situation == "Pending":
            color = "#fea95e"
        else:
            color = "red"

        return format_html(
            "<strong><p style='color: {}'>{}</p></strong>".format(color, obj.situation)
        )

    status.allow_tags = True


admin.site.register(Candidate, CandidateAdmin)
