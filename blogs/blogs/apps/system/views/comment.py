from rest_framework.viewsets import ModelViewSet

from blogs.apps.system.models import Comment
from blogs.apps.system.serializers.article import CommentSerializer


class CommentViewSet(ModelViewSet):
    # 可以加校验对评论的管理

    queryset = Comment.objects.all().order_by('id')


    serializer_class = CommentSerializer

    # 指定router动态生成路由时，提取参数的正则表达式
    lookup_value_regex = '\d+'