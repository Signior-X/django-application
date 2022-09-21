from django.contrib import admin

# Register your models here.
from .models import Application, Job, Applicant

admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Application)
