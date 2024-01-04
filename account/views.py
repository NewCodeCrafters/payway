from django.shortcuts import render
from rest_framework import views, response, permissions, status
from drf_yasg.utils import swagger_auto_schema

from account.utils import get_exchange_rate

from .models import Account
from .serializers import AccountSerializer


class NewWalletViews(views.APIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

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


class UpdateWalletView(views.APIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, account_number):
        try:
            wallet = Account.objects.get(
                account_number=account_number, user=request.user
            )
        except Account.DoesNotExist:
            return response.Response(
                {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AccountSerializer(wallet)
        data = serializer.data
        return response.Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializer_class)
    def put(self, request, account_number):
        try:
            wallet = Account.objects.get(
                account_number=account_number, user=request.user
            )
        except Account.DoesNotExist:
            return response.Response(
                {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )
        previous_currency = wallet.currency
        new_currency = request.data.get("currency", previous_currency)
        serializer = AccountSerializer(wallet, data=request.data)
        if serializer.is_valid():
            rate = get_exchange_rate(new_currency, previous_currency)

            serializer.validated_data["balance"] = rate * wallet.balance

            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
