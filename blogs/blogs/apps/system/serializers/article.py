from rest_framework import serializers

from blogs.apps.system.models import Article
from blogs.apps.system.models import Comment





class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('createtime', 'updatetime')


class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(label='作者')
    comments = CommentSerializer(read_only=True, many=True)
    # comments = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Article
        exclude = ('createtime', 'updatetime')

    # def validate_article_id(self, value):
    #
    #     try:
    #         article = Article.objects.get(id=value)
    #     except Article.DoesNotExist:
    #         raise serializers.ValidationError('文章不存在')
    #
    #     return value



class ArticleTitleSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(label='作者')
    class Meta:
        model = Article
        fields = ['title']

