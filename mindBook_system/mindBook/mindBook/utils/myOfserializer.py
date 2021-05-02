from app01.models import Label, User
from utils.serializers import UserModelSerializer, LabelModelSerializer


def label_of_data(serializer):
	for i in serializer:
		try:
			label_data = Label.objects.get(id=i['did'])
			user_data = User.objects.filter(uid=i['uid'])[0]
			user_serializer = UserModelSerializer(instance=user_data)
			label_serializer = LabelModelSerializer(instance=label_data)
			i['label'] = label_serializer.data
			i['user'] = user_serializer.data
		except:
			print('有错误')
	return serializer