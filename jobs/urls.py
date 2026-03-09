from django.urls import path
from .views import landing_page, job_list, job_detail, add_job

urlpatterns = [
    path("", landing_page, name="home"),
    path("jobs/", job_list, name="jobs"),
    path("jobs/<int:id>/", job_detail, name="job_detail"),
    path("add-job/", add_job, name="add_job"),  
]