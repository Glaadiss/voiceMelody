from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, viewsets, generics, permissions, status
from .serializers import SongSerializer, UserSerializer, RegisterSerializer
from .models import Song
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

# from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer

# from knox.views import LoginView as KnoxLoginView
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        # serializer = self.get_serializer(queryset, many=True)
        data = Song.objects.filter(user_id=request.user.id)
        return HttpResponse(
            serializers.serialize("json", data),
            content_type="text/json-comment-filtered",
        )
        # return Response(serializer.data)



# Register API

# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response(
#             {
#                 "user": UserSerializer(
#                     user, context=self.get_serializer_context()
#                 ).data,
#                 "token": AuthToken.objects.create(user)[1],
#             }
#         )


# # Login API

# class LoginAPI(KnoxLoginView):
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)


# class ChangePasswordView(generics.UpdateAPIView):

#     """
#     An endpoint for changing password.
#     """

#     serializer_class = ChangePasswordSerializer
#     model = User
#     permission_classes = (IsAuthenticated,)

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():

#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response(
#                     {"old_password": ["Wrong password."]},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )
#             if serializer.data.get("new_password") != serializer.data.get(
#                 "new_password2"
#             ):
#                 return Response(
#                     {"new_password": ["Password fields didn't match."]},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             self.object.set_password(serializer.data.get("new_password"))
#             self.object.save()
#             response = {
#                 "status": "success",
#                 "code": status.HTTP_200_OK,
#                 "message": "Password updated successfully",
#                 "data": [],
#             }

#             return Response(response)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

