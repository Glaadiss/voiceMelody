from authentication.views import CustomUserCreate, ObtainTokenPairWithColorView
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("token/obtain/", ObtainTokenPairWithColorView.as_view(), name="token_create"),
    path("user/create/", CustomUserCreate.as_view(), name="create_user"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]