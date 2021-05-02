from rest_framework import serializers
from app01.models import User, Label, LabelOf, Learn, Section


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