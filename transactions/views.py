from django.shortcuts import render
from rest_framework import views, status, permissions, response

from account.models import Account
from account.serializers import AccountSerializer

# Create your views here.


class TransferFromMainAccountView(views.APIView):
    serializer_class = ""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, account_number, currency):
        try:
            wallet = Account.objects.get(
                account_number=account_number,
                user=request.user,
                currency=currency.upper(),
            )
        except Account.DoesNotExist:
            return response.Response(
                {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = AccountSerializer(wallet)
        data = serializer.data
        return response.Response(data, status=status.HTTP_200_OK)
