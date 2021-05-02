from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class User(models.Model):
	uid = models.IntegerField(verbose_name='账户id', help_text='账户的唯一标识')
	name = models.CharField(max_length=8, verbose_name='用户昵称', help_text='只允许8位字符', default='匿名用户')
	pwd = models.CharField(max_length=16, verbose_name='用户的密码', help_text='这是用户密码')
	sex = models.BooleanField(verbose_name='用户性别', help_text='1为男，0为女', default=True)
	sign = models.CharField(max_length=32, verbose_name='用户简短的签名', help_text='字符串', default='')
	poster = models.ImageField(verbose_name='用户的头像', help_text='一个图片路径', upload_to='lsrc', default='')
	add_date = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
	mod_date = models.DateTimeField(verbose_name='每次更新时间', help_text='用来回溯', auto_now=True)


class Label(models.Model):
	"""
	标签
	"""
	title = models.CharField(max_length=32, verbose_name='标签内容', help_text='如java，python')


class LabelOf(models.Model):
	"""
	标签关系表
	"""
	mid = models.IntegerField(verbose_name='所属的模块id')
	pid = models.IntegerField(verbose_name='所属内容id')
	uid = models.IntegerField(verbose_name='标签所属用户id')
	did = models.IntegerField(verbose_name='关联的标签id')


class Learn(models.Model):
	"""
	学习计划表
	"""
	uid = models.IntegerField(verbose_name='所属用户id')
	this_id = models.IntegerField(verbose_name='学习计划id')
	parent = models.IntegerField(verbose_name='父节点', help_text='父节点为0为根节点')
	order = models.IntegerField(verbose_name='该父节点下的第几位')
	title = models.CharField(max_length=16, verbose_name='标题')
	detail = models.CharField(max_length=32, verbose_name='备注', default='')
	add_date = models.DateTimeField(verbose_name='创建的时间', default=timezone.now)
	mod_date = models.DateTimeField(verbose_name='每次更新时间', help_text='用来回溯', auto_now=True)


class Section(models.Model):
	uid = models.IntegerField(verbose_name='所属用户id')
	pid = models.IntegerField(verbose_name='该文章所属资源')
	title = models.CharField(max_length=32, verbose_name='标题')
	detail = models.TextField(verbose_name='文本内容')
	add_date = models.DateTimeField(verbose_name='创建的时间', default=timezone.now)
	mod_date = models.DateTimeField(verbose_name='每次更新时间', help_text='用来回溯', auto_now=True)


class Thinking(models.Model):
	uid = models.IntegerField(verbose_name='所属用户id')
	title = models.CharField(max_length=32, verbose_name='标题')
	detail = models.TextField(verbose_name='文本内容')
	add_date = models.DateTimeField(verbose_name='创建的时间', default=timezone.now)
	mod_date = models.DateTimeField(verbose_name='每次更新时间', help_text='用来回溯', auto_now=True)


class Navigation(models.Model):
	uid = models.IntegerField(verbose_name='所属用户id')
	title = models.CharField(max_length=32, verbose_name='导航的备注或者描述')
	src = models.TextField(verbose_name='链接')


class MyAPI(models.Model):
	uid = models.IntegerField(verbose_name='所属用户id')
	title = models.CharField(max_length=32, verbose_name='导航的备注或者描述')
	src = models.TextField(verbose_name='链接')