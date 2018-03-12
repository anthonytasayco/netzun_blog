from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Publication
from .serializers import PublicationSerializer
# Create your views here.

class PublicationAPIList(ListAPIView):

    queryset = Publication.objects.filter(active=True).order_by('-created')
    serializer_class = PublicationSerializer


def home(request):
    context = {}
    template = "web/list.html"
    return render(request, template, context)
