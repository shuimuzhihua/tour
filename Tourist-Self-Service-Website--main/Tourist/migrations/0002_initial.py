# Generated by Django 4.2.13 on 2024-07-06 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Tourist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tourist",
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
                (
                    "avatar",
                    models.ImageField(
                        blank=True, null=True, upload_to="avatars/", verbose_name="头像"
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[("regular", "普通用户"), ("vip", "VIP用户")],
                        default="regular",
                        max_length=20,
                        verbose_name="用户类型",
                    ),
                ),
                ("is_sign_in", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"verbose_name": "旅客", "verbose_name_plural": "旅客",},
        ),
        migrations.CreateModel(
            name="FrequentTraveler",
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
                ("name", models.CharField(max_length=100, verbose_name="姓名")),
                ("phone_number", models.CharField(max_length=20, verbose_name="电话")),
                (
                    "id_type",
                    models.CharField(
                        choices=[
                            ("身份证", "身份证"),
                            ("护照", "护照"),
                            ("驾照", "驾照"),
                            ("其他", "其他"),
                        ],
                        max_length=20,
                        verbose_name="证件类型",
                    ),
                ),
                ("id_number", models.CharField(max_length=50, verbose_name="证件号码")),
                ("nationality", models.CharField(max_length=100, verbose_name="国籍")),
                (
                    "gender",
                    models.CharField(
                        choices=[("男", "男"), ("女", "女")],
                        max_length=10,
                        verbose_name="性别",
                    ),
                ),
                (
                    "frequent_traveler_card",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="常旅客卡"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="frequent_travelers",
                        to="Tourist.tourist",
                        verbose_name="用户",
                    ),
                ),
            ],
            options={
                "verbose_name": "常用旅客",
                "verbose_name_plural": "常用旅客",
                "db_table": "frequent_traveler",
            },
        ),
    ]
