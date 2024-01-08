from django.shortcuts import render
from rest_framework import views, response, permissions, status
from drf_yasg.utils import swagger_auto_schema

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

        # # # Check if the user is the owner of the restaurant
        # if self.request.user != restaurant.vendor.user:
        #     return response.Response(
        #         {"error": "You are not authorized to update this restaurant profile"},
        #         status=status.HTTP_403_FORBIDDEN,
        #     )

        # get previous currency
        # new currency
        #
        serializer = AccountSerializer(wallet, data=request.data)
        if serializer.is_valid():
            # Update the name of the associated Restaurant model
            # profile.restaurant.name = request.data.get('name', profile.restaurant.name)
            # profile.restaurant.save()
            # rate = get_exchange_rate(new_currency, prevoius_currency)

            # serializer.balance = rate * serializer.balance
            # Update the RestaurantProfile instance
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
