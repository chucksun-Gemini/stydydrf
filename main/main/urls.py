from api import views, serializers
from rest_framework.routers import SimpleRouter
from django.urls import path
# 身份认证视图
from main import my_auth


urlpatterns = [
    path('generatedata/', views.generatedata),
    path('auth/', my_auth.MyAuth.as_view()),
]

router = SimpleRouter()

router.register('studetail', views.StuDetailViewSet)
router.register('publish', views.PublishViewSet)
router.register('stu', views.StuViewSet)
router.register('book', views.BookViewSet)

urlpatterns += router.urls
