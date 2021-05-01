from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from app01 import views

urlpatterns = [
		path('test/', views.Test.as_view({'get': 'list'}))
]