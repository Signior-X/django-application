from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from portal.models import Applicant
from portal.serializers import ApplicantSerializer, RecruiterSerializer


class RecruiterAPI(CreateAPIView):
    '''
    APIS and pages for the recruiter, that means us who are going
    to review the applications of the candidates
    '''

    serializer_class = ApplicantSerializer

    def get(self, request, *args, **kwargs):
        return render('index.html')

class ApplicantCreateAPI(CreateAPIView):
    '''
    Class to Manage jobs
    get - View a particular job
    post - Add a new job
    '''

    serializer_class = ApplicantSerializer

    def get_object(self, email):
        try:
            return Applicant.objects.get(email=email)
        except Applicant.DoesNotExist:
            raise Http404

    def get(self, request, email, *args, **kwargs):
        applicant = self.get_object(email)
        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        return self.create(request, *args, **kwargs)

@api_view(['GET', 'POST'])
def get_all_applicants(request):
    ''' Returns the list of all available jobs currently '''

    if request.method == 'GET':
        return render(request, template_name='index.html')
    else:
        jobs = Applicant.objects.all()
        serializer = RecruiterSerializer(jobs, many=True)
        return JsonResponse(serializer.data, safe=False)
