from rest_framework import serializers
from app01.models import User, Label, LabelOf, Learn, Section, Thinking, Navigation, MyAPI, Album, Photo, PhotoOf


class UserModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class LabelModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Label
		fields = '__all__'


class LabelOfModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = LabelOf
		fields = '__all__'


class LearnModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Learn
		fields = '__all__'


class SectionModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Section
		fields = '__all__'


class ThinkingModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Thinking
		fields = '__all__'


class NavigationModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Navigation
		fields = '__all__'


class MyAPIModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyAPI
		fields = '__all__'


class AlbumModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'


class PhotoModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = '__all__'


class PhotoOfModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = PhotoOf
		fields = '__all__'

# 每次添加serializer是添加到该位置
relation = {
	Album: AlbumModelSerializer,
	Photo: PhotoModelSerializer,
	Label: LabelModelSerializer,
	User: UserModelSerializer,
	Learn: LearnModelSerializer
}
