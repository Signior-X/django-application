from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

from rest_framework.generics import CreateAPIView

from portal.models import Job
from portal.serializers import JobSerializer

class JobCreateAPI(CreateAPIView):
    '''
    Class to Manage jobs
    get - View a particular job
    post - Add a new job
    '''

    serializer_class = JobSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return JsonResponse({serializer.errors}, safe=False)

        return self.create(request, *args, **kwargs)


def get_all_jobs(request):
    ''' Returns the list of all available jobs currently '''

    jobs = Job.objects.all()
    print(jobs.values())
    serializer = JobSerializer(jobs, many=True)
    return JsonResponse(serializer.data, safe=False)
