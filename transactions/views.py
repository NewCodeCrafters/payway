from django.shortcuts import render
from rest_framework import views, status, permissions, response
from drf_yasg.utils import swagger_auto_schema
from account.models import Account
from account.serializers import AccountSerializer
from profiles.models import Profiles
from transactions.serializers import TransferSerializer, InterTransferSerializer
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


class OtherWalletTransferViews(views.APIView):
    serializer_class = InterTransferSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, currency):
        user = request.user
        profile = user.profile
        try:
            sender_account = Account.objects.get(user=user, currency=currency.upper())
        except Account.DoesNotExist:
            return response.Response(
                {"error": "Account with this currency not available for user"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = InterTransferSerializer(data=request.data)
        if serializer.is_valid():
            try:
                recipient_account = Account.objects.get(
                    account_number=serializer.validated_data.get("account_number")
                )
                recipient_profile = recipient_account.user.profile
                amount = serializer.validated_data.get("amount")
                with transaction.atomic():
                    if sender_account.balance >= amount:
                        sender_rate = get_exchange_rate(
                            recipient_account.currency, currency.upper()
                        )
                        receiver_converted_value = sender_rate * amount

                        sender_account.balance -= amount
                        sender_account.save()
                        recipient_account.balance += receiver_converted_value
                        recipient_account.save()
                        recipient_main_balance_rate = get_exchange_rate(
                            currency.upper(), recipient_profile.currency
                        )
                        recipient_converted_value = recipient_main_balance_rate * amount
                        recipient_profile.balance += recipient_converted_value
                        recipient_profile.save()
                        sender_main_balance_rate = get_exchange_rate(
                            profile.currency, currency.upper()
                        )
                        sender_converted_value = sender_main_balance_rate * amount
                        profile.balance -= sender_converted_value
                        profile.save()
                        return response.Response(
                            {"success": "Transfer Successful"},
                            status=status.HTTP_201_CREATED,
                        )
                    else:
                        return response.Response(
                            {"error": "Insufficient Funds"},
                            status=status.HTTP_404_NOT_FOUND,
                        )
            except Account.DoesNotExist:
                return response.Response(
                    {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
                )
