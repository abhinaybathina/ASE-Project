# Generated by Django 3.0.3 on 2020-03-20 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_remove_comment_commentator'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
