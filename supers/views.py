from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super
from supers import serializers

# Create your views here.


@api_view(['GET', 'PUT', 'Delete'])
def get_super_by_id(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
@api_view(['GET','POST'])
def create_super(request):
    if request.method == 'GET':

        super_type = request.query_params.get('type')

        supers = Super.objects.all().order_by('super_type')

        if super_type:
            supers = supers.filter(super_type__type=super_type)

        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

# @api_view(['GET', 'PUT', 'DELETE'])
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     # product = Product.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         # serializer.is_valid(raise_exception=True)
#         # serializer.save()
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)





