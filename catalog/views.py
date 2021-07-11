from django.shortcuts import render
from rest_framework import viewsets
from .models import Catalog
from .serializers import CatalogSerializer

class CatalogView(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
