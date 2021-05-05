from django.utils.deprecation import MiddlewareMixin
from rest_framework.views import Response
from django.shortcuts import render, HttpResponse
# from models import UserLevel
from utils.myEnum import level


class Level(MiddlewareMixin):
	def process_request(self, request):
		# print(request.session.get('level'))
		# print(request.path)
		# print(level.admin.value)
		# print(request.method)
		if request.path == '/login/':
			pass
		elif request.session.get('level') is not level.admin.value:
			return HttpResponse('没有管理员权限')
			pass
		# return HttpResponse('维护中')

	# def process_response(self, request, response):
	# 	return response