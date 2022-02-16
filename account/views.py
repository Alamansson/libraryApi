from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, CreateNewPasswordSerializer, UserRatingSerializer
from .models import User, UserRating
from .utils import send_activation_code


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'OK', 201
            )


class ActivationView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, code, email):
        user = User.objects.get(
            email=email, activation_code=code
        )
        if not user:
            return Response('Пользователь не найден', 400)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response("Аккаунт активирован", 200)


class ForgotPasswordView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        print('request email :', request.data.get('email'))

        user = get_object_or_404(User, email=request.data.get('email'))
        user.is_active = False
        user.create_activation_code()
        user.save()
        send_activation_code(
            email=user.email, code=user.activation_code,
            status='forgot_password',
        )
        return Response('Вам отправили письмо на почту', status=200)


class CompleteResetPasswordView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CreateNewPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Вы успешно поменяли пароль', status=200
            )


class UserRatingView(APIView):

    def post(self, request):
        serializer = UserRatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Спасибо что делаете комьюнити лучше', status=200
            )


