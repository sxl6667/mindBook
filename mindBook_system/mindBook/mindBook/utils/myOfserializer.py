from app01.models import Label, User, models
from utils.serializers import UserModelSerializer, LabelModelSerializer, serializers
import warnings
from utils.serializers import relation
import traceback


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


def table_of(of_data: dict[str, models], source_data: list[dict]) -> list:
	"""将关系表中的数据转化成关系数据
	关系表中为一个一个的数字，该方法将数字取出并合成一个完整的对象
	Args:
		of_data(dict): 接收一个字典，为关系字段和models类的键值对:(关系字段, models类)
		source_data(list): 需要转化的原始数据，含关系字段，以及该关系字段的内容
	returns:
		source_data(list): 已经转化好的数据

	example:
		of_data = {'uid': UserModel, 'did': DressModel}
		source_data = {'uid': 3, 'did':6}

		return source_data = {'uid': {'id':3, 'name':tom}, 'did': {'id': 6, 'dress':'长沙'}}
	"""
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
				traceback.print_exc()
	return source_data
