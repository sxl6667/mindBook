from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app01.models import User
import utils.serializers as serializer
from rest_framework.response import Response


# Create your views here.
class UserModelViewSet(ModelViewSet):
	"""
	这是用户类
	"""
	queryset = User.objects.all()
	serializer_class = serializer.UserModelSerializer

	def retrieve(self, request, *args, **kwargs):
		if request.method == 'POST':
			data = request.data
			verify = User.objects.filter(uid=data['uid'], pwd=data['pwd'])
			if verify:
				return Response(status=200)
			return Response(status=400)
		else:
			return super().retrieve(request, *args, **kwargs)


