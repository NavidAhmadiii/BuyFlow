from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializer import LoginSerializer, UserRegisterSerializer, ProfileSerializer, Profile, TokenRefreshSerializer


# Create your views here.

class LoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny, ]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token, 'refresh_token': str(refresh), }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# use generic APIView

class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return super(UserRegisterAPIView, self).post(request, *args, **kwargs)


class ProfileAPIView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProfileDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TokenRefreshAPIView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = TokenRefreshSerializer(data=request.data)
        if serializer.is_valid():
            refresh_token = serializer.validated_data.get('refresh_token')

            # Generate new access token
            access_token = str(refresh_token.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
