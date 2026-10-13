from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # settings.AUTH_USER_MODEL : settings.py의 User모델
    # on_delete=models.CASECADE : User가 회원탈퇴하면 게시글도 모두 삭제
    # Many-to-one
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    # blank=True : 이미지를 넣지않아도 게시글 생성이 가능
    image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # 게시글과 댓글 간의 관계 (Many-to-one)
    # on_delete=models.CASCADE : 게시글이 삭제되면 댓글도 모두 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # User가 회원탈퇴하면 댓글도 모두 삭제(Many-to-one)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    