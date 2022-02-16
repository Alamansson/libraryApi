from django.urls import path
from .views import RegistrationView, ActivationView, ForgotPasswordView, CompleteResetPasswordView, UserRatingView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/<str:email>/<str:code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recover/', ForgotPasswordView.as_view()),
    path('complete_recover/', CompleteResetPasswordView.as_view()),
    path('user_rating/', UserRatingView.as_view())
    ]