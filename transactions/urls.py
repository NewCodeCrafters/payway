from django.urls import path

from . import views

urlpatterns = [
    path("transfer/", views.TransferFromMainAccountView.as_view()),
    path("other-transfer/", views.OtherWalletTransferViews.as_view()),
]
