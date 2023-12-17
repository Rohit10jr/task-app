from rest_framework import serializers
from .models import App

class AppSerializers(serializers.ModelSerializer):
    model = App
    fields= '__all__'

