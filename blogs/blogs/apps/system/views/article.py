from rest_framework.generics import ListAPIView

from rest_framework.viewsets import ModelViewSet

from blogs.apps.system.models import Article
from blogs.apps.system.serializers.article import ArticleTitleSerializer, ArticleSerializer


class ArticleTitleView(ListAPIView):

    queryset = Article.objects.all()

    serializer_class = ArticleTitleSerializer

    # pagination_class = None


class ArticleViewSet(ModelViewSet):


    queryset = Article.objects.all().order_by('id')


    serializer_class = ArticleSerializer

    # 指定router动态生成路由时，提取参数的正则表达式
    lookup_value_regex = '\d+'