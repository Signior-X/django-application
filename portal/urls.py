from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobs, name='jobs'),
    path('job/<job_id>/', views.job, name='job')
]

