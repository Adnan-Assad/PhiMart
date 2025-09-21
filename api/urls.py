from django.urls import path, include
from product.views import ProductViewset, CategoryViewSet, ReviewViewSet, ProductImageViewset
from order.views import CartViewSet, CartItemViewSet, OrderViewset
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', ProductViewset, basename='products')
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')
router.register('orders', OrderViewset , basename='orders')

product_router = routers.NestedDefaultRouter(router, 'products', lookup = 'product')
product_router.register('reviews', ReviewViewSet, basename='product-review')
product_router.register('images', ProductImageViewset, basename= 'product-images' )
# urlpatterns = router.urls
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('', include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
 

