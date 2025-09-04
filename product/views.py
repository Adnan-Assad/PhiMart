
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



class ProductViewset(ModelViewSet):

     queryset = Product.objects.all()
     serializer_class = ProductSerializer
     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
     filterset_class = ProductFilter
     pagination_class = DafaultPagination
     search_fields = ['name', 'descriptin', 'category__name']
     ordeering_fields = ['price']

 
          


     def destroy(self, request, *args, **kwargs):
          product = self.get_object()
          if product.stock >10:
               return Response({'message': 'This valu more than 10 number could not be delete!...' })
          self.perform_destroy(product)
           
          return Response(status=status.HTTP_204_NO_CONTENT)
     
class CategoryViewSet(ModelViewSet):
     queryset = Category.objects.annotate(product_count=Count('products')).all()
     serializer_class = CategorySerializer



 

# Create your views here. eta holo function based view
# @api_view(['GET', 'POST'])
# def view_products(request):
#       if request.method == 'GET':
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(products, many = True) # context={'request': request})
#         return Response(serializer.data) 
#       if request.method =='POST':
#         serializer = ProductSerializer(data=request.data) #Deserializer
#         serializer.is_valid(raise_exception=True)
        
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
      
# eta holo class based view
# class ViewProducts(APIView):
#      def get(self, request):
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(products, many = True) # context={'request': request})
#         return Response(serializer.    data) 
     
#      def post(self, request):
#         serializer = ProductSerializer(data=request.data) #Deserializer
#         serializer.is_valid(raise_exception=True)
        
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
          
# class ProductList(ListCreateAPIView):
#      queryset= Product.objects.select_related('category').all()
#      serializer_class = ProductSerializer
     # def get_queryset(self):
     #      return Product.objects.select_related('category').all()
     # def get_serializer_class(self):
     #      return ProductSerializer
     
     # def get_serializer_context(self):
     #      return {'request': self.request}



     
       


# @api_view(['GET', 'PUT', 'DELETE'])
# def view_specific_product(request, id):
#         if request.method == 'GET':

#                 product = get_object_or_404(Product, pk = id)
#                 serializer = ProductSerializer(product)
#                 return Response(serializer.data)
        
#         if request.method == 'PUT':
#              product = get_object_or_404(Product, pk = id)
#              serializer = ProductSerializer(product, data=request.data)
#              serializer.is_valid(raise_exception=True)
#              serializer.save()
#              return Response(serializer.data)
#         if request.method == 'DELETE':
#              product = get_object_or_404(Product, pk=id)
#              product.delete()
#              return Response(status=status.HTTP_204_NO_CONTENT)
        
# class ViewSpecificProduct(APIView):
#      def get(self, request,id):

#         product = get_object_or_404(Product, pk = id)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
     
#      def put(sef, request, id):
#           product = get_object_or_404(Product, pk = id)
#           serializer = ProductSerializer(product, data=request.data)
#           serializer.is_valid(raise_exception=True)
#           serializer.save()
#           return Response(serializer.data)
     
#      def delete(self, request, id):
#           product = get_object_or_404(Product, pk=id)
#           product.delete()
#           return Response(status=status.HTTP_204_NO_CONTENT)
          
          
          
             
        
# # @api_view()
# # def view_categories(request):
# #     categories = Category.objects.annotate(product_count=Count('products')).all()
# #     serializer = CategorySerializer(categories,  many = True)

# #     return Response(serializer.data)

# class ViewCategories(APIView):
#      def get(self, request):
          
#           categories = Category.objects.annotate(product_count=Count('products')).all()
#           serializer = CategorySerializer(categories,  many = True)
#           return Response(serializer.data)
#      def post(self, request):
#           serializer =CategorySerializer(data=request.data)
#           serializer.is_valid(raise_exception=True)
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_201_CREATED)

          


# # @api_view()
# # def view_specific_category(request, id):
# #       category = get_object_or_404(Category , pk = id)
# #       serializer = CategorySerializer(category)
# #       return Response(serializer.data)

# class CategoryDetails(RetrieveUpdateDestroyAPIView):
#      queryset = category = Category.objects.annotate(product_count = Count('products')).all()
#      serializer_class = CategorySerializer
     





# # class ViewSpecificCategory(APIView):
# #      def get(self,request, id):
# #           category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(), pk=id)
# #           serializer = CategorySerializer(category)
# #           return Response(serializer.data)
     
# #      def put(self, request, id):
# #           category = get_object_or_404(Category.objects.annotate(product_count = Count('products')).all(), pk=id)
# #           serializer = CategorySerializer(category, data = request.data)
# #           serializer.is_valid(raise_exception=True)
# #           serializer.save()
# #           return Response(serializer.data)
     
# #      def delete(self, request, id):
# #           category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=id)
# #           category.delete()
# #           return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(ModelViewSet):
      
     serializer_class = ReviewSerializer

     def get_queryset(self):
          return Review.objects.filter(product_id=self.kwargs['product_pk'])

     def get_serializer_context(self):
          return {'product_id':self.kwargs['product_pk']}