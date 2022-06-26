from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import MoleculeApi
from .serializers import ApiSerializer
from rest_framework import filters

class MoleculeApiView(ListAPIView):
    queryset = MoleculeApi.objects.all()
    serializer_class = ApiSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['LSN_Number']