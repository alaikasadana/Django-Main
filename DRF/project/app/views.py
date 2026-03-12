from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Data
from .serializers import DataSerializer
from django.http import HttpResponse
# Create your views here.
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def data_list(req):
    if req.method=='POST':
        json = req.body
        # print(json)
        # print(type(json))
        stream = io.BytesIO(json)
        # print(stream)
        # print(type(stream))
        p_data = JSONParser().parse(stream)
        # print(p_data)
        # print(type(p_data))
        serializer = DataSerializer(data=p_data)
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            data = {
                'msg': "Object create....."
            }
            json = JSONRenderer().render(data)
            return HttpResponse(json,content_type='application/json') 
        else:
            json = JSONRenderer().render(serializer.errors)
            return HttpResponse(json,content_type='application/json')
              
    x = Data.objects.all()
    serialize = DataSerializer(x,many=True)
    print(serialize)
    print(serialize.data)
    json = JSONRenderer().render(serialize.data)
    print(json)
    return HttpResponse(json,content_type='application/json')
    
    



def data_detail(req,pk):
    x = Data.objects.get(id=pk)
    serialize = DataSerializer(x)
    print(serialize)
    print(serialize.data)
    json = JSONRenderer().render(serialize.data)
    print(json)
    return HttpResponse(json,content_type='application/json')