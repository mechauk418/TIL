from django.urls import path, include
from .views import CookieTokenRefreshView, CookieTokenObtainPairView # Import the above views


app_name='accounts'


urlpatterns = [
    path('auth/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]