from django.contrib import admin
from .models import Banner
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'slug']

admin.site.register(Banner, BannerAdmin)
