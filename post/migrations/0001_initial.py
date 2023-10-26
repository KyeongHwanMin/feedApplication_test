# Generated by Django 4.2.6 on 2023-10-26 13:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="post",
            fields=[
                (
                    "content_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="id",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("facebook", "facebook"),
                            ("twitter", "twitter"),
                            ("instagram", "instagram"),
                            ("threads", "threads"),
                        ],
                        max_length=15,
                        verbose_name="유형",
                    ),
                ),
                ("title", models.CharField(max_length=128, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                ("hashtags", models.CharField(max_length=15, verbose_name="해시태그")),
                ("view_count", models.PositiveIntegerField(verbose_name="조회 수")),
                ("like_count", models.PositiveIntegerField(verbose_name="좋아요 수")),
                ("share_count", models.PositiveIntegerField(verbose_name="공유 수")),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
                ),
            ],
        ),
    ]
