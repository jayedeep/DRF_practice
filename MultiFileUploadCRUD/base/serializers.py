from rest_framework import serializers
from .models import Product,ProductPhoto

class ProductSerializer(serializers.ModelSerializer):
    product_photos = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ['name','description','product_photos']


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['product','file','file_name']

class ProductPhotoMultiFileSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.FileField(allow_empty_file=True, required=False))
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(),
                                                  many=False, write_only=True)

    def create(self, validated_data):
        files = validated_data.get('files')
        product_id = validated_data.get('product_id')

        product_photo_instances = []
        for file in files:
            product_photo_instances.append(ProductPhoto(product=product_id,file=file,file_name=file.name))
        ProductPhoto.objects.bulk_create(product_photo_instances)

        serializer = ProductSerializer(product_id)
        return validated_data
