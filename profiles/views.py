from django.shortcuts import render
from rest_framework import response, status, permissions, views

from .serializers import ProfileSerializer


class GetUpdateProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    # get, put, post, delete,
    def get(self, request):
        return response.Response({"success": "You got in"})

    def put(self, request):
        return response.Response({"success": "You got in"})
