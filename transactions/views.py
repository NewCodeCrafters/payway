from django.shortcuts import render
from rest_framework import views, status, permissions, response
from drf_yasg.utils import swagger_auto_schema
from account.models import Account
from account.serializers import AccountSerializer
from profiles.models import Profiles
from transactions.serializers import TransferSerializer
from django.db import transaction

from transactions.utils import get_exchange_rate


# Create your views here.


class TransferFromMainAccountView(views.APIView):
    serializer_class = TransferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            profile = Account.objects.filter(
                user=request.user,
            )
        except Account.DoesNotExist:
            return response.Response(
                {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = AccountSerializer(profile, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request):
        profile = request.user.profile
        main_balance = profile.balance
        main_currency = profile.currency
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            account_number = serializer.validated_data.get("account_number")
            transaction_type = serializer.validated_data.get("transaction_type")
            print(transaction_type)
            amount = serializer.validated_data.get("amount")
            try:
                with transaction.atomic():
                    account = Account.objects.get(
                        user=request.user, account_number=account_number
                    )
                    if transaction_type == "DEPOSIT":
                        if main_balance >= amount:
                            rate = get_exchange_rate(account.currency, main_currency)
                            converted_value = amount * rate
                            account.balance += converted_value
                            account.save()
                            profile.net_balance -= amount
                            profile.save()
                        else:
                            return response.Response(
                                {"error": "Insufficient main balance for deposit"},
                                status=status.HTTP_400_BAD_REQUEST,
                            )
                    elif transaction_type == "WITHDRAWAL":
                        if account.balance >= amount:
                            rate = get_exchange_rate(
                                main_currency,
                                account.currency,
                            )
                            converted_value = amount * rate
                            account.balance -= converted_value
                            profile.net_balance += converted_value
                            profile.save()
                        else:
                            return response.Response(
                                {"error": "Insufficient balance for withdrawal"},
                                status=status.HTTP_400_BAD_REQUEST,
                            )
                    else:
                        return response.Response(
                            {"error": "Invalid transaction type"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
            except Account.DoesNotExist:
                return response.Response(
                    {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
                )

            # Assuming TransferSerializer saves the data to the database
            serializer.save(user=request.user)

            return response.Response(
                {"message": "Transaction successful"}, status=status.HTTP_201_CREATED
            )

        return response.Response(
            {"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST
        )
