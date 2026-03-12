from rest_framework import serializers
from .models import Data

class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    email=serializers.CharField(max_length=20)
    age=serializers.IntegerField()
    contact=serializers.IntegerField()


# class EmpSerializers(serializers.Serializer):
#     class meta :
#         model = Data
#         fields = "__all__"