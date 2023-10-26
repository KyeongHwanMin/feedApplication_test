import uuid
from django.db import models

from accounts.models import User

SOCIAL_CHOICE = (
    ("facebook", "facebook"),
    ("twitter", "twitter"),
    ("instagram", "instagram"),
    ("threads", "threads"),
)


class Post(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="post", verbose_name="작성자"
    )
    content_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id"
    )
    type = models.CharField(
        max_length=15, choices=SOCIAL_CHOICE, blank=True, verbose_name="유형"
    )
    title = models.CharField(max_length=128, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    hashtags = models.CharField(max_length=15, blank=True, verbose_name="해시태그")
    view_count = models.PositiveIntegerField(default=0, verbose_name="조회 수")
    like_count = models.PositiveIntegerField(default=0, verbose_name="좋아요 수")
    share_count = models.PositiveIntegerField(default=0, verbose_name="공유 수")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정 날짜")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜")
