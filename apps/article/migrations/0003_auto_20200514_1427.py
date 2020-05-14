# Generated by Django 3.0.5 on 2020-05-14 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_auto_20200514_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(help_text='标签名称', max_length=50, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.AlterModelOptions(
            name='commentarticleuserrel',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, help_text='类别', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='article.Category', verbose_name='类别'),
        ),
        migrations.AlterField(
            model_name='article',
            name='comment_m2m',
            field=models.ManyToManyField(help_text='评论(m2m)', related_name='comment_m2m_articles', through='article.CommentArticleUserRel', to=settings.AUTH_USER_MODEL, verbose_name='评论(m2m)'),
        ),
        migrations.AlterField(
            model_name='commentarticleuserrel',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.Article'),
        ),
        migrations.AlterField(
            model_name='commentarticleuserrel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(help_text='标签', related_name='articles', to='article.Tag', verbose_name='标签'),
        ),
    ]