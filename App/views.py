from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# FRONTEND
# Home
def home(request):
    return render(request, "home.html")


# Candidate registration
def register(request):
    if request.method == "POST":
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered Successfully!")
            return HttpResponseRedirect("/")
        else:
            return render(request, "register.html", {"form": form})

    else:
        form = CandidateForm()
        return render(request, "register.html", {"form": form})


# BACKEND


# HR - Home page (backend)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    context = {
        "data_read": Candidate.objects.all(),
    }
    return render(request, "backend.html", context)


# Access candidates (individually)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request, id):
    # data = Candidate.objects.get(pk=id)
    # form = CandidateForm(instance=data)
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
    #     form.fields[field].disabled = True
    #     form.fields["file"].widget.attrs.update({"style": "display: none;"})
    #     form.fields["image"].widget.attrs.update({"style": "display: none;"})
    # context = {"form": form}
    # return render(request, "candidate.html", context)

    candidate = Candidate.objects.get(pk=id)
    return render(request, "candidate.html", {"candidate": candidate})
