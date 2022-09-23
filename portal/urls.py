from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_all_applicants, name='recruiter - index'),
    path('api/recruiter/', views.RecruiterAPI.as_view(), name="Recruiter APIs"),
    path('api/applicant/', views.ApplicantAPI.as_view() , name='Applicants APIs'),
    path('api/applicant/<email>/', views.ApplicantAPI.as_view(), name="Fetch application details from email"),
]

