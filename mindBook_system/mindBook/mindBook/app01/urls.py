from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from app01 import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('login/', views.UserModelViewSet.as_view({'post': 'retrieve'})),
	path('album/img/<int:pk>/', views.PhotoAPIView.as_view())
]
router = DefaultRouter()
router.register('user', views.UserModelViewSet)
router.register('label', views.LabelModelViewSet)
router.register('label-link', views.LabelOfModelViewSet)
router.register('learn', views.LearnModelViewSet)
router.register('section', views.SectionModelViewSet)
router.register('thinking', views.ThinkingModelViewSet)
router.register('navigation', views.NavigationModelViewSet)
router.register('api', views.MyAPIModelViewSet)
router.register('album', views.AlbumModelViewSet)
router.register('photo', views.PhotoModelViewSet)
urlpatterns += router.urls
