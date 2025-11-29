from django.contrib import admin
from .models import Duyuru, Icerik


@admin.register(Duyuru)
class DuyuruAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'tarih')


@admin.register(Icerik)
class IcerikAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    search_fields = ('title',)