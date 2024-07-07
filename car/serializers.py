from rest_framework import serializers
from .models import Car



class Car_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['maker','catigory','image','model','year','color','price',
                  'mileage','transmission','fuel_type','body_style']

