from rest_framework import serializers
from .models import Catalog

class CatalogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalog
        fields = ('id','url','name','material','price')