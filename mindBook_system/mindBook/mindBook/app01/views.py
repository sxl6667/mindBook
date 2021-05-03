from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from app01.models import User, Label, LabelOf, Learn, Section, Thinking, Navigation, MyAPI, Album, Photo, PhotoOf, \
	Resource
import utils.serializers as serializer
from utils.serializers import relation
import utils.myOfserializer as myOf
from rest_framework.response import Response
from rest_framework.views import APIView


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
			return Response(status=203)
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
	relation = {
		'pid': Learn,
		'uid': User,
		'did': Label
	}

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset(self.get_queryset())
		data = self.get_serializer(queryset, many=True)
		# data = myOf.label_of_data(data.data)
		data = myOf.table_of(self.relation, data.data)
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


class SectionModelViewSet(ModelViewSet):
	"""
	这是文章视图
	"""
	queryset = Section.objects.all()
	serializer_class = serializer.SectionModelSerializer
	filterset_fields = ['pid']


class ThinkingModelViewSet(ModelViewSet):
	"""
	这是想法视图
	"""
	queryset = Thinking.objects.all()
	serializer_class = serializer.ThinkingModelSerializer
	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['add_date']


class NavigationModelViewSet(ModelViewSet):
	queryset = Navigation.objects.all()
	serializer_class = serializer.NavigationModelSerializer


class MyAPIModelViewSet(ModelViewSet):
	queryset = MyAPI.objects.all()
	serializer_class = serializer.MyAPIModelSerializer


class AlbumModelViewSet(ModelViewSet):
	queryset = Album.objects.all()
	serializer_class = serializer.AlbumModelSerializer


class PhotoModelViewSet(ModelViewSet):
	"""
	关系表的使用:
	relation : 关系表，为关联字段和model
	relation_2 : models和其序列化器
	"""
	queryset = PhotoOf.objects.all()
	serializer_class = serializer.PhotoOfModelSerializer
	relation = {
		'aid': Album,
		'pid': Photo
	}

	def list(self, request, *args, **kwargs):
		try:
			queryset = self.filter_queryset(self.get_queryset())
			serializer = self.get_serializer(queryset, many=True)
			data = myOf.table_of(self.relation, serializer.data)
			return Response(data=data)
		except:
			return super().list(request, *args, **kwargs)


class PhotoAPIView(APIView):
	def post(self, request, pk):
		data = request.data
		instance = serializer.PhotoModelSerializer(data=data)
		instance.is_valid(raise_exception=True)
		instance.save()
		data = {
			'aid': pk,
			'pid': instance.data['id']
		}
		instance = my_save(data, serializer.PhotoOfModelSerializer)
		print(instance)
		return Response(status=200, data=instance)


def my_save(data: {}, model_serializer) -> {}:
		instance = model_serializer(data=data)
		instance.is_valid(raise_exception=True)
		instance.save()
		return instance.data


class ResourceModelViewSet(ModelViewSet):
	queryset = Resource.objects.all()
	serializer_class = serializer.ResourceModelSerializer
