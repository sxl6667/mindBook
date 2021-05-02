from rest_framework import serializers
from app01.models import User, Label, LabelOf


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
