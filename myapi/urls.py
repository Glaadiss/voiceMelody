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

]