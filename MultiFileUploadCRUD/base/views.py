from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product,ProductPhoto
from .serializers import ProductSerializer,ProductPhotoSerializer,ProductPhotoMultiFileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPhotoViewSet(ModelViewSet):
    queryset = ProductPhoto.objects.all()
    serializer_class = ProductPhotoSerializer


class ProductPhotoMultiFile(APIView):

    def get(self,request,id=None,format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        print(">>>>>>>>request",request.data)
        serializer = ProductPhotoMultiFileSerializer(data = request.data)
        product_id = request.data.get('product_id')
        if serializer.is_valid():
            serializer.save()
            print("product_id",product_id)
            products = Product.objects.get(id=product_id)
            serializer = ProductSerializer(products)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

        return Response(serializer.data)