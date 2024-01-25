from rest_framework import viewsets
from .models import Product, Category, Cart, Order, UserProfile
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, OrderSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .services import handle_uploaded_file
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(ProductViewSet, self).get_permissions()


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        return super(CategoryViewSet, self).get_permissions()


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = [IsAuthenticated]


class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            handle_uploaded_file(request.FILES['file'])
            return Response(file_serializer.data, status=201)
        else:
            return Response(file_serializer.errors, status=400)
