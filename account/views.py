from django.shortcuts import render
from rest_framework import views, response, permissions

from .models import Account
from .serializers import AccountSerializer
