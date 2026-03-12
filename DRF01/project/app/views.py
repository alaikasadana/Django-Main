

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from .models import Data

# Create your views here.
@api_view(['GET', 'POST'])
def stu_list(req):
    if req.method=='POST':
        serializer = DataSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    stu = Data.objects.all()
    serializer = DataSerializer(stu, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','PATCH','DELETE'])
def stu_details(req,pk):
	u_id = Data.objects.filter(id=pk)
	if u_id:
		if req.method=='PUT':
			snippet = Data.objects.get(id=pk)
			serializer = DataSerializer(snippet, data=req.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		elif req.method=='PATCH':
			snippet = Data.objects.get(id=pk)
			serializer = DataSerializer(snippet, data=req.data, partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		elif req.method=='DELETE':
			snippet = Data.objects.get(id=pk)
			snippet.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		
		snippet = Data.objects.get(id=pk)
		serializer = DataSerializer(snippet)
		return Response(serializer.data)
	else:
		return Response({}, status=status.HTTP_400_BAD_REQUEST)