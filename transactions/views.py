from django.shortcuts import render
from rest_framework import views, status, permissions, response

from account.models import Account
from account.serializers import AccountSerializer
from profiles.models import Profiles
from transactions.serializers import TransferSerializer

# Create your views here.


class TransferFromMainAccountView(views.APIView):
    serializer_class = TransferSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            profiles = Account.objects.filter(
                user=request.user,
            )
        except Account.DoesNotExist:
            return response.Response(
                {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = AccountSerializer(profiles, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        #     profile = request.user.profile
        #     balance = profile.balance
        #     from_currency = profile.currency

        return response.Response()
