from django.contrib import admin
from .models import Articles,Category,Tag

from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from django.utils.html import format_html
# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    def image_tag(self,obj):
        if obj.img:
            return format_html('<img src="{}" style="width:50px;height:50px;"/>'.format(obj.img.url))
        return ''
    image_tag.allow_tags = True
    image_tag.short_description = '文章配图'
    # 表头
    list_display = ('title','author','image_tag','abstract','visited','created_at')
    # # 搜索
    # search_fields = ('title','author','abstract','content')
    # # 筛选
    # list_filter = list_display



admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Category,)
admin.site.register(Tag,)
