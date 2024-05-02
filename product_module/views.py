from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .paginations import CustomPagination
from .serializer import ProductSerializer, ProductCreateSerializer
from .filters import ProductFilter
from .models import Product


# Create your views here.


class ProductListView(ListAPIView):
    queryset = Product.objects.all().order_by('price', )
    serializer_class = ProductSerializer
    search_fields = ['name', 'descriptions']
    filter_class = ProductFilter
    pagination_class = CustomPagination


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    serializer_class = ProductCreateSerializer
