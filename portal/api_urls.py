from django.urls import path

from portal.apis import jobs

urlpatterns = [
    path('jobs/', jobs.get_all_jobs, name='index'),
]
