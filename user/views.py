from django.contrib.auth import get_user_model, login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserAccountSerializer
UserModel = get_user_model()

        
class LoginUserTokenObtainView(TokenObtainPairView):
	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			return Response(serializer.validated_data, status=status.HTTP_200_OK)
		return Response({'msg': 'Password or Email invalid'}, status=status.HTTP_409_CONFLICT)

class RegisterUserTokenObtainView(APIView):
	serializer_class = UserAccountSerializer
	serializer_token_obtain = RefreshToken	
	def post(self, request, *args, **kwargs):
		user_serializer = self.serializer_class(data=request.data)
		if user_serializer.is_valid():
			user = user_serializer.save()
			tokens = self.serializer_token_obtain.for_user(user)
			return Response({'refresh': str(tokens), 'access': str(tokens.access_token)}, status=status.HTTP_200_OK)
		return Response(user_serializer.errors)

class LogoutUserAPIView(APIView):
	authentication_classes = [JWTAuthentication]
	def get(self, request, *args, **kwargs):
		refresh = RefreshToken.for_user(request.user)
		return Response({'message': 'Logout exist'}, status=status.HTTP_200_OK)

class EditUserAPIView(APIView):
	serializer_class = UserAccountSerializer
	authentication_classes = [JWTAuthentication]
	def post(self, request, *args, **kwargs):
		user_serializer = self.serializer_class(request.user, data=request.data)
		if user_serializer.is_valid():
			user_serializer.save()
			return Response(user_serializer.data, status=status.HTTP_200_OK)
		return Response(user_serializer.errors)

