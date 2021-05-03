from app01.models import Label, User, models
from utils.serializers import UserModelSerializer, LabelModelSerializer, serializers
import warnings
from utils.serializers import relation

def label_of_data(serializer):

	warnings.warn('这个方法不够灵活,建议使用table_of', DeprecationWarning)
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


def table_of(of_data: dict[str, models], source_data: list[dict]):
	for i in source_data:
		for key, val in i.items():
			try:
				if key != 'id':
					if key == 'uid':
						a = of_data[key].objects.filter(uid=val)
					else:
						a = of_data[key].objects.filter(id=val)
					serializer = relation[of_data[key]](instance=a, many=True)
					i[key] = serializer.data
			except:
				print('出现异常')
	return source_data