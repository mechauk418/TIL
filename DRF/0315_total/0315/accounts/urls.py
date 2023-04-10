from django.urls import path, include
from .views import kakao_callback, KakaoLogin # Import the above views

urlpatterns = [
    path("kakao/callback/", kakao_callback, name="kakao_callback"),
    path(
        "kakao/login/finish/", KakaoLogin.as_view(), name="kakao_login_todjango"
    ),
]