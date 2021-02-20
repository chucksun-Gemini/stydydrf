from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class MyAuth(APIView):
    permission_classes = [AllowAny, ]

    # 注册普通账号
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        # 查询账号在数据模型中是否存在
        user = User.objects.filter(username=username).first()
        # 如果存在，返回前端提示：用户名已存在
        if user:
            return Response({"sign_in": False, "detail": "用户名已存在"})
        # 如果不存在，create_user新建普通账户，create_superuser新建管理员用户
        user_obj = User.objects.create_user(username=username, password=password)
        # 返回前端提示：注册成功
        return Response({"sign_in": True, "detail": "注册成功"})

    # 登陆账号:设置浏览器session
    def get(self, request):
        username = request.params["username"]
        password = request.params["password"]
        # 校验用户名和密码，若未通过，返回none
        user_obj = auth.authenticate(username=username, password=password)
        # 如果用户名或密码错误，返回前端提示信息
        if not user_obj:
            return Response({"log_in": False, "detail": "用户名或密码错误"})
        # 验证通过，login方法设置浏览器session
        auth.login(request, user_obj)
        return Response({"log_in": True, "detail": "登陆成功"})

    # 注销退出登陆：清理session
    def delete(self, request):
        # logout方法，清理session,不清除csrftoken
        auth.logout(request)
        return Response({"log_in": False, "detail": "注销成功"})
