from django.shortcuts import render
from rest_framework import views, response, permissions, status
from drf_yasg.utils import swagger_auto_schema

from .models import Account
from .serializers import AccountSerializer


class NewWalletViews(views.APIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        user = request.user
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            # currency = serializer.data["currency"]
            serializer.save(
                user=user,
            )
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
