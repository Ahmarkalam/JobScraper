from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    """
    Form for manually adding jobs through the website
    """
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'link']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Senior Python Developer',
                'maxlength': '300'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Google, Microsoft, Startup Inc.',
                'maxlength': '200'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Remote, New York, Bangalore',
                'maxlength': '200'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://company.com/careers/job-123',
            }),
        }
        
        labels = {
            'title': 'Job Title',
            'company': 'Company Name',
            'location': 'Location',
            'link': 'Application Link (URL)',
        }
        
        help_texts = {
            'title': 'Enter the full job title as it appears in the posting',
            'company': 'Name of the hiring company or organization',
            'location': 'City, country, or "Remote" for remote positions',
            'link': 'Direct link to the job application page',
        }
    
    def clean_link(self):
        """Validate that the link is a proper URL"""
        link = self.cleaned_data.get('link')
        if link and not link.startswith(('http://', 'https://')):
            raise forms.ValidationError('Please enter a valid URL starting with http:// or https://')
        return link
    
    def clean_title(self):
        """Ensure title is not empty and has reasonable length"""
        title = self.cleaned_data.get('title')
        if title and len(title.strip()) < 5:
            raise forms.ValidationError('Job title must be at least 5 characters long')
        return title.strip()
