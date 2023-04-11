from django.urls import path, include
from .views import kakao_callback, KakaoLogin, google_callback, GoogleLogin # Import the above views

urlpatterns = [
    path("kakao/callback/", kakao_callback, name="kakao_callback"),
    path(
        "kakao/login/finish/", KakaoLogin.as_view(), name="kakao_login_todjango"
    ),
    path("google/callback/", google_callback, name="google_callback"),
    path(
        "google/login/finish/", GoogleLogin.as_view(), name="google_login_todjango"
    ),
]