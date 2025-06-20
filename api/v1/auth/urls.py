from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.v1.auth.views import (
    NuxtCookieTokenRefreshView,
    NuxtLoginView,
    NuxtLogoutView,
    set_csrf_token,
)

urlpatterns = [
    # Nuxt/Web endpoints (cookie-based)
    path("nuxt/csrf/", set_csrf_token),
    path("nuxt/login/", NuxtLoginView.as_view()),
    path("nuxt/logout/", NuxtLogoutView.as_view()),
    path("nuxt/refresh/", NuxtCookieTokenRefreshView.as_view()),
    # path("nuxt/", include("dj_rest_auth.urls")),
    # Mobile endpoints (token-based)
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
