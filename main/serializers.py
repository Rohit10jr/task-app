from rest_framework import serializers
from .models import App

# serializers for app
class AppSerializers(serializers.ModelSerializer):
    model = App
    fields= '__all__'

