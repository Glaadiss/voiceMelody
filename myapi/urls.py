from django.urls import include, path
from rest_framework import routers
from . import views

# from .views import RegisterAPI, LoginAPI, ChangePasswordView

# from knox import views as knox_views

router = routers.DefaultRouter()
router.register(r"song", views.SongViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # path("api/register/", RegisterAPI.as_view(), name="register"),
    # path("api/login/", LoginAPI.as_view(), name="login"),
    # path("api/logout/", knox_views.LogoutView.as_view(), name="logout"),
    # path("api/logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    # path("api/change-password/", ChangePasswordView.as_view(), name="change-password"),
]