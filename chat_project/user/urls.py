from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'user'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('auth/', Auth.as_view(), name='auth'),
    path('auth/refresh/', TokenRefreshView.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout')
]