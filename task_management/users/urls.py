from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserView , UserRegisterView , UserLoginView , UserRoleView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('',UserView.as_view(),name='user-list'),
    path('register/',UserRegisterView.as_view(),name='user-register'),
    path('login/',UserLoginView.as_view(),name='user-login'),
    path('role/',UserRoleView.as_view(),name='user-role'),
]