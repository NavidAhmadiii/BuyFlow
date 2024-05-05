from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView
import requests
import json
from .models import Order, OrderDetail
from .serializer import OrderSerializer, OrderDetailSerializer

# Create your views here.

USER = get_user_model()


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(CreateAPIView):
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderSerializer


class AddToCart(CreateAPIView):
    serializer_class = OrderDetailSerializer

    def post(self, request, price=None, *args, **kwargs):
        product_id = request.data.get('product_id')
        count = request.data.get('count')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ViewCart(ListAPIView):
    serializer_class = OrderDetailSerializer

    # # دریافت سبد خرید کاربر فعلی
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            try:
                return user.order_set.first().order_detail.all()
            except Order.DoesNotExist:
                return OrderDetail.objects.none()
        return OrderDetail.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "سبد خرید خالی است."}, status=status.HTTP_204_NO_CONTENT)


class RemoveFromCart(RetrieveDestroyAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field = 'pk'  # نام فیلدی که برای جستجو بر روی آن انجام می‌شود، مثلاً شناسه محصول

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()  # دریافت شیء مربوطه بر اساس شناسه ارسالی
        self.perform_destroy(instance)  # حذف شیء
        return Response({'message': 'محصول مورد نظر با موفقیت از سبد خرید شما حذف شد.'},
                        status=status.HTTP_204_NO_CONTENT)  # پاسخ موفقیت‌آمیز


# class Checkout(APIView):
#     permission_classes = [IsAuthenticated]
#
#     # @login_required
#     def post(self, request):
#         # دریافت اطلاعات از درخواست
#         delivery_address = request.data.get('delivery_address')
#         payment_method = request.data.get('payment_method')
#
#         # یافتن سبد خرید کاربر
#         order = Order.objects.filter(user=request.user, is_paid=False).first()
#
#         if order:
#             order.is_paid = True
#             order.save()
#
#             return Response({"message": "سفارش با موفقیت ثبت شد."}, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": "سبد خرید خالی است."}, status=status.HTTP_204_NO_CONTENT)


# Zarinpal
# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = 'YOUR_PHONE_NUMBER'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8080/verify/'


class PaymentView(APIView):

    def post(self, request):
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Description": description,
            "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}

        try:
            response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)
            if response.status_code == 200:
                response_data = response.json()
                if response_data['Status'] == 100:
                    return Response({
                        'status': True,
                        'payment_url': ZP_API_STARTPAY + str(response_data['Authority']),
                        'authority': response_data['Authority']
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'status': False, 'code': str(response_data['Status'])},
                                    status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.Timeout:
            return Response({'status': False, 'code': 'timeout'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.ConnectionError:
            return Response({'status': False, 'code': 'connection error'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # متد GET برای تایید پرداخت استفاده می‌شود
        authority = request.query_params.get('authority')
        if authority:
            data = {
                "MerchantID": settings.MERCHANT,
                "Amount": amount,
                "Authority": authority,
            }
            data = json.dumps(data)
            headers = {'content-type': 'application/json', 'content-length': str(len(data))}
            response = requests.post(settings.ZP_API_VERIFY, data=data, headers=headers)
            if response.status_code == 200:
                response_data = response.json()
                if response_data['Status'] == 100:
                    return Response({'status': True, 'RefID': response_data['RefID']}, status=status.HTTP_200_OK)
                else:
                    return Response({'status': False, 'code': str(response_data['Status'])},
                                    status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': False, 'code': 'authority not provided'}, status=status.HTTP_400_BAD_REQUEST)
