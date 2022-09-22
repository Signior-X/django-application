from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_all_applicants, name='recruiter - index'),
    path('applicant/', views.ApplicantCreateAPI.as_view() , name='applicants'),
    path('applicant/<email>', views.ApplicantCreateAPI.as_view(), name="Fetch application details from email"),
]

