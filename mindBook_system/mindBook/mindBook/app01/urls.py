from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from app01 import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('login/', views.UserModelViewSet.as_view({'post': 'retrieve'})),
]
router = DefaultRouter()
router.register('user', views.UserModelViewSet)
router.register('label', views.LabelModelViewSet)
router.register('label-link', views.LabelOfModelViewSet)
router.register('learn', views.LearnModelViewSet)
urlpatterns += router.urls
