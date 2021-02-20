from rest_framework import viewsets
from rest_framework.decorators import action
from api import models, serializers
from rest_framework.response import Response
from django.shortcuts import HttpResponse
# 可导入AllowAny,IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
# 导入局部访问频率控制
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class StuDetailViewSet(viewsets.ModelViewSet):
    queryset = models.StuDetail.objects.all()
    serializer_class = serializers.StuDetailSerializer
    # 传入局部身份验证: 任何用户均可进入
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"], detail=False)
    def showsheet(self, request):
        """此函数功能是获取身高大于175的学生详情返回客户端"""
        studetail_obj = self.get_queryset().filter(height__gt=175)
        serializer = self.get_serializer(instance=studetail_obj, many=True)
        print(request.META)
        return Response(serializer.data)

    @action(methods=["PUT"], detail=True)
    def editsheet(self, request, pk):
        """此函数功能PUT方法修改学生详情，但会显示修改的时间"""
        studetail_obj = self.get_object()
        serializer = self.get_serializer(instance=studetail_obj, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PublishViewSet(viewsets.ModelViewSet):
    queryset = models.Publish.objects.all()
    serializer_class = serializers.PublishSerializer


class StuViewSet(viewsets.ModelViewSet):
    queryset = models.Stu.objects.all()
    serializer_class = serializers.StuSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


def generatedata(request):
    # # 增加StuDetail表内数据
    # models.StuDetail.objects.create(id=1, birthday='1999-12-9', height=165.4, gender=1)
    # models.StuDetail.objects.create(id=2, birthday='1987-8-8', height=175.5, gender=2)
    # models.StuDetail.objects.create(id=3, birthday='1990-7-10', height=180.3, gender=0)
    #
    # # 增加Stu表内数据
    # models.Stu.objects.create(id=1, name='sam', stu_detail_id=2)
    # models.Stu.objects.create(id=2, name='duke', stu_detail_id=1)
    # models.Stu.objects.create(id=3, name='jane', stu_detail_id=3)
    #
    # # 增加Publish表内数据
    # models.Publish.objects.create(id=1, name='central publisher')
    # models.Publish.objects.create(id=2, name='social publisher')
    #
    # # 增加Book表中数据
    # # 添加方法一：直接添加id值
    # models.Book.objects.create(id=1, name='math', publish_id=2)
    # models.Book.objects.create(id=2, name='chinese', publish_id=2)
    # # 添加方法二：添加object对象
    # publish_1 = models.Publish.objects.first()
    # models.Book.objects.create(id=3, name='english', publish=publish_1)

    # 增加多对多中间表stu_book中对应关系
    # stu_1 = models.Stu.objects.first()
    # stu_2 = models.Stu.objects.filter(id=2).first()
    # stu_3 = models.Stu.objects.last()
    #
    # book_1 = models.Book.objects.first()
    # book_2 = models.Book.objects.filter(id=2).first()
    # book_3 = models.Book.objects.last()

    # stu_1.book.add(book_1, book_2)
    # stu_2.book.add(book_2)
    # 此处有*号，与改操作对比记忆
    # stu_3.book.add(*[book_1, book_2])

    return HttpResponse('处理结束')