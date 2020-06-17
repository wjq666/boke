from django.conf.urls import url
from rest_framework.routers import DefaultRouter


from system.views import user, article, comment

urlpatterns = [

url(r'^login/$', user.RegisterView.as_view()),
url(r'^article/$', article.ArticleTitleView.as_view()),

]


router = DefaultRouter()
router.register('contents', article.ArticleViewSet, basename='article')
urlpatterns += router.urls
router = DefaultRouter()
router.register('comment', comment.CommentViewSet, basename='comment')
urlpatterns += router.urls
for urls in urlpatterns:
    print(urls)