from django.contrib import admin

from .models import Group
from .models import Post


@admin.register(Group)
class GroupAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date', 'group',)
    empty_value_display = '-пусто-'