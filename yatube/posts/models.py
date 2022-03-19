from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group (models.Model):
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('Адрес', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='group_posts',
        verbose_name='Группа'
    )

    class Meta:
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']
