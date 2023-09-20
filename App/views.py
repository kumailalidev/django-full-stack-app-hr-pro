from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.db.models.functions import Concat
from django.db.models import Value as P
from .forms import CandidateForm, EmailForm, Chat_candidateForm
from .models import Candidate, Email, Chat_candidate
import pdfkit


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
    # Global Filter
    if "f" in request.GET:
        f = request.GET["f"]
        all = Candidate.objects.filter(Q(job__iexact=f) | Q(gender__iexact=f)).order_by(
            "-created_at"
        )

    # Global search
    elif "q" in request.GET:
        q = request.GET["q"]
        all = (
            Candidate.objects.annotate(name=Concat("firstname", P(" "), "lastname"))
            .filter(
                Q(name__icontains=q)
                | Q(firstname__icontains=q)
                | Q(lastname__icontains=q)
                | Q(email__icontains=q)
                | Q(phone__icontains=q)
            )
            .order_by("-created_at")
        )
    else:
        all = Candidate.objects.all().order_by("-created_at")

    # Pagination
    paginator = Paginator(all, 3)
    page = request.GET.get("page")
    all_candidate = paginator.get_page(page)

    # Counters
    total = all.count()
    frontend = all.filter(job="FR-22")
    backend = all.filter(job="BA-10")
    fullstack = all.filter(job="FU-15")

    context = {
        "candidates": all_candidate,
        "total": total,
        "frontend": frontend,
        "backend": backend,
        "fullstack": fullstack,
    }

    return render(request, "backend.html", context)


# Access candidates (individually)
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    return render(request, "candidate.html", {"candidate": candidate})


# Delete
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delete(request, id):
    x = Candidate.objects.values_list("email", flat=True)
    y = Chat_candidate.objects.filter(candidate_email__in=x)
    candidate = Candidate.objects.get(id=id)
    for data in y:
        if data.candidate_email in candidate.email:
            candidate.delete()
            Chat_candidate.objects.exclude(candidate_email__in=x).delete()
            messages.success(request, "Candidate deleted successfully")
            return HttpResponseRedirect("/backend")
        else:
            candidate.delete()
            messages.success(request, "Candidate deleted successfully")
            return HttpResponseRedirect("/backend")


# EXPORT TO PDF
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request, id):
    c = Candidate.objects.get(pk=id)
    cookies = request.COOKIES
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
        # Without cookies login page will be printed
        "cookie": [
            ("csrftoken", cookies["csrftoken"]),
            ("sessionid", cookies["sessionid"]),
        ],
    }
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # Method 2 (Customized, but requires an external file)
    pdf_name = c.firstname + "_" + c.lastname + ".pdf"
    pdf = pdfkit.from_url(
        "http://localhost:8000/pdf/" + str(c.id),
        False,
        options=options,
        configuration=config,
    )
    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-disposition"] = f"attachment; filename={pdf_name}"
    return response


# Template PDF
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pdf(request, id):
    candidate = Candidate.objects.get(id=id)
    return render(request, "pdf.html", {"candidate": candidate})


# SEND EMAIL
def email(request):
    if request.method == "POST":
        # Save the message in DB (No ModelForm)
        to_db = Email(
            employee=request.POST.get("employee"),
            status=request.POST.get("status"),
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        to_db.save()

        form = EmailForm(request.POST)
        # Company subject
        company = "Django Mastery"
        # Send email via forms.py
        if form.is_valid():
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            mail = EmailMessage(subject, message, company, [email])
            mail.send()

            messages.success(request, "Email sent successfully !")
            return HttpResponseRedirect("/backend")
        else:
            form = EmailForm()
            return render(request, {"form": form})


# CHATBOX
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def chat_candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    chat_candidate = Chat_candidate.objects.all().order_by("-dt")
    list_users = User.objects.all()
    form = Chat_candidateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("chat_candidate", id=candidate.id)
    context = {
        "form": form,
        "chat_candidate": chat_candidate,
        "list_users": list_users,
        "candidate": candidate,
    }

    return render(request, "chat_candidate.html", context)


# CODE NO LONGER REQUIRED

# *) This code was present inside backend view

# Filter (individual)
# if request.method == "POST":
#     job = request.POST.get("job")
#     filter = Candidate.objects.filter(job=job)
#     context = {"candidates": filter}
#     return render(request, "backend.html", context)  # NOTE: Breaks pagination

# *) This code was present inside candidate view

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

# *) This code was present inside index view

# Method 1 (Simple, but exports the all the content) Generated via URL
# pdf = pdfkit.from_url(
#     "http://localhost:8000/" + str(c.id),
#     False,
#     options=options,
#     configuration=config,
# )
# response = HttpResponse(pdf, content_type="application/pdf")
# response["Content-disposition"] = "attachment; filename=candidate.pdf"
# return response
