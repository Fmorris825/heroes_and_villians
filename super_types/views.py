from ast import Return
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.serializers import SuperTypeSerializer
from supers.models import Super
from supers.serializers import SuperSerializer
from .models import SuperType
from super_types import serializers
# Create your views here.

@api_view(['GET', 'POST'])
def get_super_types(request):
    if request.method == 'GET':
        super_types = SuperType.objects.all()
        serializer = serializers.SuperTypeSerializer(super_types, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_201_CREATED)



@api_view(['GET','PUT'])
def super_type_list(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)