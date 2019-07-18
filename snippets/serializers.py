from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(default='python', choices=LANGUAGE_CHOICES)
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         '''创造一个新的序列实例  通过一个确认的数据'''
#
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """ 更新数据实例 通过一个字典"""
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.save()
#         return instance


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']



class SnippetSerializer(serializers.ModelSerializer):
    '''
    使用封装好的数据序列化类
    重要的是要记住ModelSerializer类不会做任何特别神奇的事情，它们只是创建序列化类的快捷方式：
    '''
    # 创建的代码片段与用户相关联 只允许所有者读取
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']




