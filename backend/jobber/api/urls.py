from django.urls import path
from .views import RegisterUserView, LoginUserView

urlpatterns = [
    path("auth/register/", RegisterUserView.as_view(), name='register'),
    path("auth/login/", LoginUserView.as_view(), name="login"),
]