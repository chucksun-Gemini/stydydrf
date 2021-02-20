from django.db import models


class Stu(models.Model):
    name = models.CharField(max_length=12, unique=True)

    # on_delete为联级删除，外键在一对多的多中设置， stu_detail值代表StuDetail表中的一行
    stu_detail = models.ForeignKey('StuDetail', on_delete=models.CASCADE)

    # 多对多方法一：多对多的中间表由此语句隐式创建，即stu_book表
    book = models.ManyToManyField('Book')


class StuDetail(models.Model):
    # 日期格式为：2020-10-1
    birthday = models.DateField()
    # 允许最大值为999.9，总位数为4，小数位为1
    height = models.DecimalField(max_digits=4, decimal_places=1)

    gender_choices = (  # 适用于可选项固定且少，可不新增表的情况
        (0, 'female'),  # 强制写3，数据库也接受
        (1, 'male'),
        (2, 'secret'),
    )
    # views.py中取法：res = models.StuDetail.gender_choices[0][1]，返回female
    # 										  将可选项导入进来
    gender = models.SmallIntegerField(choices=gender_choices)


class Book(models.Model):
    name = models.CharField(max_length=12, unique=True)
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE)


class Publish(models.Model):
    name = models.CharField(max_length=50, unique=True)
