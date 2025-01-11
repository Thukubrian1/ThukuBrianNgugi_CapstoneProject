from rest_framework import viewsets
from rest_framework import permissions, filters
from .models import Category, Product
from rest_framework.authtoken.models import Token
from .serializers import CategorySerializer, ProductSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Product, User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@login_required
def product_management(request):
    return render(request, 'product-management/index.html')

@login_required
def product_search(request):
    return render(request, 'product-search/search.html')

def product_management(request):
    return render(request, 'product-management/index.html')

def product_search(request):
    return render(request, 'product-search/search.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    # To allow admins to view and manage all users, but restrict regular users
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            self.permission_classes = [AllowAny]  # Can be accessed by authenticated users
        elif self.action == 'create':
            self.permission_classes = [AllowAny]  # Only admins can create users
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [AllowAny]  # Only admins can update or delete users
        return super().get_permissions()
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'category__name']  # Search by product name or category name
    ordering_fields = ['price', 'stock_quantity']  # Allow ordering by price or stock quantity

# View for User Registration
class UserRegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": UserSerializer(user).data,
                "message": "User registered successfully!"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View for User Login (authentication)
class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                # Here you could return a token (JWT, for example)
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            else:
                return Response({"error": "Invalid credentials"}, status=400)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        except CustomUser.DoesNotExist:
            return Response({
                "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)
def perform_create(self, serializer):
        # Automatically associate the created product with the current user
        serializer.save(created_by=self.request.user)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'product-management/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('product-management')  # Redirect to the product search page after login
    else:
        form = AuthenticationForm()
    return render(request, 'product-management/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')