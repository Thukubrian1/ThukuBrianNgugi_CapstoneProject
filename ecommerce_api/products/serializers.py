from rest_framework import serializers
from .models import Product, Category, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        # Custom logic for user update (ensure password is properly handled if updated)
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created_by', 'created_date']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'