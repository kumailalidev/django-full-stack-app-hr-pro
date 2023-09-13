from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.core.paginator import Paginator
from django.db.models import Q
import pdfkit

# Concatenate (F-name and L-name)
from django.db.models.functions import Concat  # Concatenate
from django.db.models import Value as P  # (P = Plus)


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
    # Filter (individual)
    # if request.method == "POST":
    #     job = request.POST.get("job")
    #     filter = Candidate.objects.filter(job=job)
    #     context = {"candidates": filter}
    #     return render(request, "backend.html", context)  # NOTE: Breaks pagination

    # Global Filter
    if request.method == "POST":
        job = request.POST.get("job")
        gender = request.POST.get("gender")
        filter = Candidate.objects.filter(Q(job=job) | Q(gender=gender))
        # Counters
        total = Candidate.objects.all().count()
        frontend = Candidate.objects.filter(job="FR-22")
        backend = Candidate.objects.filter(job="BA-10")
        fullstack = Candidate.objects.filter(job="FU-15")
        context = {
            "candidates": filter,
            "total": total,
            "frontend": frontend,
            "backend": backend,
            "fullstack": fullstack,
        }
        return render(request, "backend.html", context)  # NOTE: Breaks pagination

    # Global search
    elif "q" in request.GET:
        q = request.GET["q"]
        all_candidate_list = (
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
        all_candidate_list = Candidate.objects.all().order_by("-created_at")

    # Pagination
    paginator = Paginator(all_candidate_list, 10)
    page = request.GET.get("page")
    all_candidate = paginator.get_page(page)

    # Counters
    total = Candidate.objects.all().count()
    frontend = Candidate.objects.filter(job="FR-22")
    backend = Candidate.objects.filter(job="BA-10")
    fullstack = Candidate.objects.filter(job="FU-15")

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
