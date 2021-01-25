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
