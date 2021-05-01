from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from app01 import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('test/', views.Test.as_view({'get': 'list'})),
	path('login/', views.UserModelViewSet.as_view({'post': 'retrieve'}))
]
router = DefaultRouter()
router.register('user', views.UserModelViewSet)
urlpatterns += router.urls
