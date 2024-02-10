from django.shortcuts import render
from rest_framework import response, status, permissions, views
from drf_yasg.utils import swagger_auto_schema

from .models import Profiles
from .serializers import ProfileSerializer


class GetUpdateProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    # get, put, post, delete,
    def get(self, request):
        user = request.user
        profile = Profiles.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return response.Response(serializer.data)

    @swagger_auto_schema(request_body=ProfileSerializer)
    def put(self, request):
        user = request.user
        profile = Profiles.objects.get(user=user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
