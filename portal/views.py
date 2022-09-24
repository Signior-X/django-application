from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from portal.models import Applicant
from portal.serializers import ApplicantSerializer, RecruiterSerializer, ApplicantStatusUpdateSerializer


@api_view(['GET', 'POST'])
def get_all_applicants(request):
    """
    Part 1 -> List all the applicants

    Returns
    --------
    GET - Renders the page of our single page app
    POST - The JSONResponse object having all available applicants currently
    """

    if request.method == 'GET':
        return render(request, template_name='index.html')
    else:
        jobs = Applicant.objects.all()
        serializer = RecruiterSerializer(jobs, many=True)
        return JsonResponse(serializer.data, safe=False)


class RecruiterAPI(ListAPIView):
    """
    BONUS 2 - Pagination and filtering all done here
    For Recruiter to review the applications of the candidates
    """

    queryset = Applicant.objects.all()
    serializer_class = RecruiterSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        """ No need to define get, it will automatically handle the pagination
        We are using limit set pagination """

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """ Filtering the query set based on the degree we get from parameters """
        
        queryset = Applicant.objects.all()
        degree = self.request.query_params.get('degree')
        if degree is not None:
            queryset = queryset.filter(degree=degree)
        
        status = self.request.query_params.get('status')
        if status is not None:
            queryset = queryset.filter(status=status)

        return queryset



class ApplicantAPI(CreateAPIView):
    """ CRUD to manage applications by applicants

    post - Create the applicants data using post api (Part 2)
    get - Read an applicants data using "email"
    put - Update the applicants data using "email" (Part 3 and Accepted - Rejected)
    delete - Delete an application
    """

    serializer_class = ApplicantSerializer

    def get_object(self, email):
        try:
            return Applicant.objects.get(email=email)
        except Applicant.DoesNotExist:
            raise Http404

    def get(self, request, email, *args, **kwargs):
        """ Reads an applicants data from email """

        applicant = self.get_object(email)
        serializer = ApplicantSerializer(applicant)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """ Create an application from data came in parameters """

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        return self.create(request, *args, **kwargs)

    def put(self, request, email, *args, **kwargs):
        """ Upadate an applicant's data from email """

        applicant = self.get_object(email)
        serializer = ApplicantStatusUpdateSerializer(applicant, data=request.data)

        if serializer.is_valid():
            print("valid")
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email, format=None):
        """ Deletes the application associated with email """

        applicant = self.get_object(email)
        applicant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

