import time
import requests
from jobs.models import Job

APP_ID = "4834034f"
APP_KEY = "1ea41c23fe6e0d13290bcb07d2287f73"

countries = ["in", "us", "gb", "ca", "au", "sg"]

keywords = [
    "software engineer",
    "python developer",
    "java developer",
    "backend developer",
    "frontend developer",
    "full stack developer",
    "data analyst",
    "data scientist",
    "project manager",
    "business analyst",
    "management trainee",
]

def scrape_jobs():

    for country in countries:

        for keyword in keywords:

            for page in range(1,4):

                url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/{page}"

                params = {
                    "app_id": APP_ID,
                    "app_key": APP_KEY,
                    "what": keyword,
                    "results_per_page": 20
                }

                response = requests.get(url, params=params)
                data = response.json()

                for job in data.get("results", []):

                    Job.objects.get_or_create(
                        title=job.get("title", ""),
                        company=job.get("company", {}).get("display_name", ""),
                        location=job.get("location", {}).get("display_name", ""),
                        link=job.get("redirect_url", "")
                    )

                time.sleep(1)