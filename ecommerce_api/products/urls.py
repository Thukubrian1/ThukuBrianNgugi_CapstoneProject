from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, UserRegisterAPIView, UserLoginAPIView
from .import views

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('api/', include(router.urls)),  # This will automatically route the API views
    path('api/register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('api/login/', UserLoginAPIView.as_view(), name='user_login'),
    path('product-management/', views.product_management, name='index'),
    path('product-search/', views.product_search, name='search'), 
    path('register/', views.register,name='register'),
    path('login/', views.login_view, name='login'),       # Add login URL
    path('logout/', views.logout_view, name='logout'),    # Add logout URL
]
