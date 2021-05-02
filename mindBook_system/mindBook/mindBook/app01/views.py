from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app01.models import User, Label, LabelOf, Learn
import utils.serializers as serializer
import utils.myOfserializer as myOf
from rest_framework.response import Response


# Create your views here.
class UserModelViewSet(ModelViewSet):
	"""
	这是用户类
	"""
	queryset = User.objects.all()
	serializer_class = serializer.UserModelSerializer
	filterset_fields = ['uid']

	def retrieve(self, request, *args, **kwargs):
		if request.method == 'POST':
			data = request.data
			verify = User.objects.filter(uid=data['uid'], pwd=data['pwd'])
			if verify:
				return Response(status=200)
			return Response(status=400)
		else:
			return super().retrieve(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		data = request.data
		verify = User.objects.filter(uid=data['uid'])
		if verify:
			return Response(status=400, data={'msg': '账号已存在'})
		return super().create(request, *args, **kwargs)


class LabelModelViewSet(ModelViewSet):
	"""
	这是标签视图
	"""
	queryset = Label.objects.all()
	serializer_class = serializer.LabelModelSerializer


class LabelOfModelViewSet(ModelViewSet):
	"""
	这是标签关系视图，
	重写list方法
	"""
	queryset = LabelOf.objects.all()
	serializer_class = serializer.LabelOfModelSerializer
	filterset_fields = ['uid']

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		data = self.get_serializer(queryset, many=True)
		data = myOf.label_of_data(data.data)
		# print(data)
		# return super().list(request, *args, **kwargs)
		return Response(data=data)


class LearnModelViewSet(ModelViewSet):
	"""
	这是学习计划视图
	uid: 为所属用户
	this_id: 为所属学习计划
	parent: 为父节点id
	"""
	queryset = Learn.objects.all()
	serializer_class = serializer.LearnModelSerializer
	filterset_fields = ['uid', 'this_id', 'parent']

