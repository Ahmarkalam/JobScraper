from django.core.management.base import BaseCommand
from jobs.models import Job

class Command(BaseCommand):
    help = 'Load sample jobs into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading sample jobs...')
        
        sample_jobs = [
            {"title": "Senior Python Developer", "company": "Google", "location": "Remote", "link": "https://careers.google.com/jobs/1"},
            {"title": "Full Stack Engineer", "company": "Microsoft", "location": "Seattle, WA", "link": "https://careers.microsoft.com/jobs/1"},
            {"title": "Data Scientist", "company": "Amazon", "location": "New York, NY", "link": "https://amazon.jobs/en/jobs/1"},
            {"title": "Frontend Developer React", "company": "Meta", "location": "Remote", "link": "https://metacareers.com/jobs/1"},
            {"title": "Backend Java Developer", "company": "Netflix", "location": "Los Gatos, CA", "link": "https://jobs.netflix.com/jobs/1"},
            {"title": "DevOps Engineer", "company": "Apple", "location": "Cupertino, CA", "link": "https://jobs.apple.com/jobs/1"},
            {"title": "Machine Learning Engineer", "company": "OpenAI", "location": "San Francisco, CA", "link": "https://openai.com/careers/1"},
            {"title": "Software Engineer", "company": "Stripe", "location": "Remote", "link": "https://stripe.com/jobs/1"},
            {"title": "Data Analyst", "company": "Airbnb", "location": "San Francisco, CA", "link": "https://careers.airbnb.com/jobs/1"},
            {"title": "Product Manager", "company": "Uber", "location": "San Francisco, CA", "link": "https://uber.com/careers/1"},
            {"title": "UI/UX Designer", "company": "Adobe", "location": "Remote", "link": "https://adobe.com/careers/1"},
            {"title": "Cloud Engineer AWS", "company": "Amazon", "location": "Seattle, WA", "link": "https://amazon.jobs/jobs/2"},
            {"title": "Security Engineer", "company": "Cloudflare", "location": "London, UK", "link": "https://cloudflare.com/careers/1"},
            {"title": "Mobile Developer iOS", "company": "Apple", "location": "Cupertino, CA", "link": "https://jobs.apple.com/jobs/2"},
            {"title": "Android Developer", "company": "Google", "location": "Mountain View, CA", "link": "https://careers.google.com/jobs/2"},
            {"title": "Solutions Architect", "company": "Microsoft", "location": "Remote", "link": "https://careers.microsoft.com/jobs/2"},
            {"title": "Business Analyst", "company": "Deloitte", "location": "New York, NY", "link": "https://deloitte.com/careers/1"},
            {"title": "Project Manager", "company": "Accenture", "location": "Chicago, IL", "link": "https://accenture.com/careers/1"},
            {"title": "Database Administrator", "company": "Oracle", "location": "Austin, TX", "link": "https://oracle.com/careers/1"},
            {"title": "QA Engineer", "company": "Tesla", "location": "Palo Alto, CA", "link": "https://tesla.com/careers/1"},
            {"title": "Python Backend Developer", "company": "Spotify", "location": "Remote", "link": "https://spotify.com/jobs/1"},
            {"title": "React Developer", "company": "Twitter", "location": "San Francisco, CA", "link": "https://twitter.com/careers/1"},
            {"title": "Data Engineer", "company": "LinkedIn", "location": "Sunnyvale, CA", "link": "https://linkedin.com/jobs/1"},
            {"title": "Full Stack JavaScript Developer", "company": "Shopify", "location": "Toronto, Canada", "link": "https://shopify.com/careers/1"},
            {"title": "Senior Java Developer", "company": "IBM", "location": "Bangalore, India", "link": "https://ibm.com/jobs/1"},
            {"title": "AI/ML Research Engineer", "company": "DeepMind", "location": "London, UK", "link": "https://deepmind.com/careers/1"},
            {"title": "Site Reliability Engineer", "company": "Dropbox", "location": "Remote", "link": "https://dropbox.com/jobs/1"},
            {"title": "Blockchain Developer", "company": "Coinbase", "location": "San Francisco, CA", "link": "https://coinbase.com/careers/1"},
            {"title": "Game Developer Unity", "company": "Epic Games", "location": "Remote", "link": "https://epicgames.com/careers/1"},
            {"title": "Cybersecurity Analyst", "company": "Cisco", "location": "San Jose, CA", "link": "https://cisco.com/careers/1"},
            {"title": "Junior Python Developer", "company": "Infosys", "location": "Pune, India", "link": "https://infosys.com/careers/1"},
            {"title": "Software Development Engineer", "company": "Salesforce", "location": "Remote", "link": "https://salesforce.com/careers/1"},
            {"title": "Technical Support Engineer", "company": "Zendesk", "location": "Remote", "link": "https://zendesk.com/jobs/1"},
            {"title": "Systems Administrator", "company": "RedHat", "location": "Raleigh, NC", "link": "https://redhat.com/jobs/1"},
            {"title": "Backend Node.js Developer", "company": "PayPal", "location": "Chennai, India", "link": "https://paypal.com/careers/1"},
            {"title": "Angular Frontend Developer", "company": "SAP", "location": "Bangalore, India", "link": "https://sap.com/jobs/1"},
            {"title": "Laravel PHP Developer", "company": "WordPress", "location": "Remote", "link": "https://wordpress.com/jobs/1"},
            {"title": "Digital Marketing Manager", "company": "HubSpot", "location": "Remote", "link": "https://hubspot.com/careers/1"},
            {"title": "Product Designer", "company": "Figma", "location": "San Francisco, CA", "link": "https://figma.com/careers/1"},
            {"title": "Technical Writer", "company": "Atlassian", "location": "Sydney, Australia", "link": "https://atlassian.com/jobs/1"},
            {"title": "Network Engineer", "company": "Juniper Networks", "location": "Sunnyvale, CA", "link": "https://juniper.net/careers/1"},
            {"title": "IoT Developer", "company": "Samsung", "location": "Seoul, South Korea", "link": "https://samsung.com/careers/1"},
            {"title": "Embedded Systems Engineer", "company": "Intel", "location": "Santa Clara, CA", "link": "https://intel.com/jobs/1"},
            {"title": "Scrum Master", "company": "Jira", "location": "Remote", "link": "https://jira.com/careers/1"},
            {"title": "Business Intelligence Analyst", "company": "Tableau", "location": "Seattle, WA", "link": "https://tableau.com/jobs/1"},
            {"title": "ETL Developer", "company": "Informatica", "location": "Redwood City, CA", "link": "https://informatica.com/careers/1"},
            {"title": "SAP Consultant", "company": "Cap Gemini", "location": "Mumbai, India", "link": "https://capgemini.com/jobs/1"},
            {"title": "Salesforce Developer", "company": "Vlocity", "location": "Remote", "link": "https://vlocity.com/careers/1"},
            {"title": "AWS Cloud Architect", "company": "CloudBees", "location": "Remote", "link": "https://cloudbees.com/jobs/1"},
            {"title": "Kubernetes Engineer", "company": "Rancher", "location": "Remote", "link": "https://rancher.com/careers/1"}
        ]
        
        added_count = 0
        for job_data in sample_jobs:
            job, created = Job.objects.get_or_create(
                title=job_data['title'],
                company=job_data['company'],
                defaults={
                    'location': job_data['location'],
                    'link': job_data['link']
                }
            )
            if created:
                added_count += 1
                self.stdout.write(self.style.SUCCESS(f'✓ Added: {job.title}'))
        
        total_jobs = Job.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\n✅ Done! Added {added_count} new jobs'))
        self.stdout.write(self.style.SUCCESS(f'📊 Total jobs in database: {total_jobs}'))