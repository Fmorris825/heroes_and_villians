from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.models import Super
from supers.serializers import SuperSerializer
from .models import SuperType
from super_types import serializers
# Create your views here.

@api_view(['GET'])
def super_type_list(request, pk):
    if request.method == 'GET':
        super_type = SuperType.objects.filter(pk=pk)
        supers = Super.objects.filter(super_type=super_type)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = ProductSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.errors, status=status.HTTP_201_CREATED)