from rest_framework import serializers
from .models import Users

class BackendSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields =['id', 'name', 'email', 'telephone']