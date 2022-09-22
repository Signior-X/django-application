from django.urls import path, include

from portal.views import applicant
from portal.views import recruiter

urlpatterns = [
    path('', applicant.index, name='index'),
    path('job/<job_id>/', applicant.job, name='job'),
    path('recruiter/<job_id>', recruiter.job, name='recruiter_job'),
]

