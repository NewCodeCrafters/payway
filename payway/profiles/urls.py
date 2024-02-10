from django.urls import path
from . import views

urlpatterns = [path("update-profile/", views.GetUpdateProfileView.as_view())]
