
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.pagination import DafaultPagination
from api.permissions import IsAdminOrReadOnly, FullDjangoModelPermission
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly


class ProductViewset(ModelViewSet):

     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
     filterset_class = ProductFilter
     pagination_class = DafaultPagination
     search_fields = ['name', 'description']
     ordeering_fields = ['price', 'updated_at']
     # permission_classes = [IsAdminUser]
     # permission_classes = [IsAuthenticated]
     permission_classes = [IsAdminOrReadOnly]
     # permission_classes = [FullDjangoModelPermission]
     # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

     def destroy(self, request, *args, **kwargs):
          product = self.get_object()
          if product.stock >10:
               return Response({'message': 'This valu more than 10 number could not be delete!...' })
          self.perform_destroy(product)
           
          return Response(status=status.HTTP_204_NO_CONTENT)
     
class CategoryViewSet(ModelViewSet):
     permission_classes = [IsAdminOrReadOnly]
     queryset = Category.objects.annotate(product_count=Count('products')).all()
     serializer_class = CategorySerializer




class ReviewViewSet(ModelViewSet):
      
     serializer_class = ReviewSerializer

     def perform_create(self, serializer):
          serializer.save(user= self.request.user)

     def get_queryset(self):
          return Review.objects.filter(product_id=self.kwargs['product_pk'])

     def get_serializer_context(self):
          return {'product_id':self.kwargs['product_pk']}