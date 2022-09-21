from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    ''' Home page of the App '''
    return render(request, 'index.html')

def jobs(request):
    ''' View all job postings '''
    return render(request, 'applicants/jobs.html')

def job(request, job_id):
    ''' Job page to apply for that job '''
    return render(request, 'applicants/job.html')
