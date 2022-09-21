from django.http import HttpResponse, JsonResponse

from portal.models import Job
from portal.serializers import JobSerializer

def get_all_jobs(request):
    jobs = Job.objects.all()
    print(jobs.values())
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse(serializer.data, safe=False)
    
