from rest_framework import serializers
from decimal import Decimal
from product.models import Category, Product, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']
    product_count = serializers.IntegerField(read_only=True)

  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category','price_with_tax'] # other

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )
  
    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    

    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("price could not be negative")
        return price
    
   
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comments', 'ratings']
        read_only_fields = ['user', 'product']

    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review
       