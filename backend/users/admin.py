from django.contrib import admin

from .models import Subscribe, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
    )
    search_fields = ('email', 'username')
    list_filter = ('email', 'username',)
    empty_value_display = '-пусто-'


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'author')
    search_fields = ('user',)
    list_filter = ('user',)
    empty_value_display = '-пусто-'
