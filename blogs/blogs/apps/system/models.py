from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'


    def __str__(self):
        return self.username


class Article(models.Model):

    title = models.CharField(max_length=100, null=True, default=None, verbose_name="标题")
    content = models.TextField(default='', verbose_name='文章内容')
    image = models.CharField(null=True, max_length=100, default=None, verbose_name="文章封面")
    createtime = models.DateTimeField(auto_now_add=True, null=True,verbose_name="创建日期")
    updatetime = models.DateTimeField(auto_now=True, null=True,verbose_name="修改日期")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name='用户ID')


    class Meta:
        db_table = "tb_article"
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-createtime']

    def __str__(self):
        return self.title


class Comment(models.Model):

    content = models.CharField(max_length=1000,default='', verbose_name='评论内容')
    createtime = models.DateTimeField(auto_now_add=True, null=True, verbose_name="创建日期")
    updatetime = models.DateTimeField(auto_now=True, null=True, verbose_name="修改日期")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", default=None,verbose_name="文章ID")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", default=None, verbose_name="用户ID")

    class Meta:
        db_table = "article_comment"
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ['-createtime']  # 指明默认排序

    def __str__(self):
        return self.content