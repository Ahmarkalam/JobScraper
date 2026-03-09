from django.shortcuts import render, get_object_or_404
from .models import Job
from django.core.paginator import Paginator


def landing_page(request):
    total_jobs = Job.objects.count()
    total_companies = Job.objects.values("company").distinct().count()

    context = {
        "total_jobs": total_jobs,
        "total_companies": total_companies
    }

    return render(request, "landing.html", context)


def job_list(request):

    jobs = Job.objects.all().order_by("-created_at")

    query = request.GET.get("q")
    location = request.GET.get("location")

    if query:
        jobs = jobs.filter(title__icontains=query)

    if location:
        jobs = jobs.filter(location__icontains=location)

    paginator = Paginator(jobs, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # predefined job categories
    job_roles = [
        "Software Engineer",
        "Python Developer",
        "Java Developer",
        "Data Analyst",
        "Data Scientist",
        "Management Trainee",
        "Business Analyst",
        "Project Manager",
        "Marketing",
        "Sales"
    ]

    # predefined locations
    locations = [
        "Remote",
        "India",
        "California",
        "New York",
        "San Francisco",
        "Seattle",
        "Austin",
        "London",
        "Berlin",
        "Toronto",
        "Sydney"
    ]

    return render(request, "jobs.html", {
        "jobs": page_obj,
        "job_roles": job_roles,
        "locations": locations
    })