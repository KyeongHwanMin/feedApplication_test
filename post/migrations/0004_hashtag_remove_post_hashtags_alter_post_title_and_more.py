# Generated by Django 4.2.6 on 2023-10-26 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_alter_post_hashtags_alter_post_like_count_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hashtag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="post",
            name="hashtags",
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=255, verbose_name="제목"),
        ),
        migrations.AlterField(
            model_name="post",
            name="type",
            field=models.CharField(
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
        migrations.AddField(
            model_name="post",
            name="hashtags",
            field=models.ManyToManyField(blank=True, to="post.hashtag"),
        ),
    ]
