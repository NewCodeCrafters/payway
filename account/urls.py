from django.urls import path
from . import views

urlpatterns = [path("add-new-wallet", views.NewWalletViews.as_view())]
