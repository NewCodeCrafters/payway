from django.urls import path

from . import views

urlpatterns = [
    path("transfer/", views.TransferFromMainAccountView.as_view()),
]
