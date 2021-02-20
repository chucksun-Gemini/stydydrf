from rest_framework import serializers
from api import models


class StuDetailSerializer(serializers.ModelSerializer):
    '''StuDetail表序列器'''
    class Meta:
        model = models.StuDetail
        fields = "__all__"


class PublishSerializer(serializers.ModelSerializer):
    '''Publish表序列器'''

    class Meta:
        model = models.Publish
        fields = "__all__"


class StuSerializer(serializers.ModelSerializer):
    '''Stu表序列器'''

    class Meta:
        model = models.Stu
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    '''Book表序列器'''

    class Meta:
        model = models.Book
        fields = "__all__"
