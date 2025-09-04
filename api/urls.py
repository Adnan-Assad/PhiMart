from django.urls import path, include
from product.views import ProductViewset, CategoryViewSet, ReviewViewSet
from order.views import CartViewSet, CartItemViewSet
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewset, basename='products')
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')

product_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
# urlpatterns = router.urls
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
]
 

