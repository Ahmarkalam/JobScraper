from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "jobs"

    def ready(self):
        try:
            from scraper import scrape_jobs
            scrape_jobs()
        except:
            pass