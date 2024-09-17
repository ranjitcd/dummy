from rest_framework import serializers
from .models import Watches



class WatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watches
        fields = ['id','name','brand','price','image','updated','created']