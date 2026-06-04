from rest_framework import viewsets
from .models import JobApplication
from .serializers import JobApplicationSerializer

class JobApplicationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Job Applications.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = JobApplication.objects.all().order_by('-applied_date') # Newest applications first
    serializer_class = JobApplicationSerializer