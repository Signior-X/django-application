from django.shortcuts import render
from django.http import HttpResponse

def job(request, job_id):
    ''' See job applications for the current job '''
    return render(request, 'recruiter/job.html')
