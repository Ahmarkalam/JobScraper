from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import JobForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


def landing_page(request):
    total_jobs = Job.objects.count()
    total_companies = Job.objects.values("company").distinct().count()

    context = {
        "total_jobs": total_jobs,
        "total_companies": total_companies
    }

    return render(request, "landing.html", context)


def job_list(request):
    # Start with all jobs ordered by most recent
    jobs = Job.objects.all().order_by("-created_at")

    # Get filter parameters
    query = request.GET.get("q", "").strip()
    location = request.GET.get("location", "").strip()
    company = request.GET.get("company", "").strip()

    # Apply filters if provided
    if query:
        # Search in both title and company for better results
        jobs = jobs.filter(
            Q(title__icontains=query) | Q(company__icontains=query)
        )

    if location:
        jobs = jobs.filter(location__icontains=location)

    if company:
        jobs = jobs.filter(company__icontains=company)

    # Pagination - 15 jobs per page
    paginator = Paginator(jobs, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Predefined job categories (quick filters)
    job_roles = [
        "Software Engineer",
        "Python Developer",
        "Java Developer",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "Data Analyst",
        "Data Scientist",
        "Machine Learning",
        "DevOps Engineer",
        "Business Analyst",
        "Project Manager",
        "Product Manager",
        "UI/UX Designer",
    ]

    # Predefined locations (quick filters)
    locations = [
        "Remote",
        "India",
        "United States",
        "United Kingdom",
        "Canada",
        "Australia",
        "Singapore",
        "New York",
        "San Francisco",
        "London",
        "Toronto",
        "Sydney",
        "Bangalore",
        "Berlin",
    ]

    context = {
        "jobs": page_obj,
        "job_roles": job_roles,
        "locations": locations,
        "query": query,
        "location_filter": location,
        "company_filter": company,
    }

    return render(request, "jobs.html", context)


def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    
    context = {
        "job": job
    }
    
    return render(request, "job_detail.html", context)


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_job(request):
    """
    View for manually adding a job posting
    Only accessible to admin/staff users
    """
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job posted successfully! It will appear in the listings.')
            return redirect('add_job')  # Redirect to show empty form again
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = JobForm()
    
    # Get recent jobs for preview
    recent_jobs = Job.objects.all().order_by('-created_at')[:5]
    
    context = {
        'form': form,
        'recent_jobs': recent_jobs,
    }
    
    return render(request, 'add_job.html', context)
