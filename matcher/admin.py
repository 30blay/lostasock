from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Sock, Match

admin.site.site_header = 'Lostasock Administration'
admin.site.site_title = admin.site.site_header
admin.site.index_title = 'Home'

# Register your models here.
@admin.register(Sock)
class SockAdmin(admin.ModelAdmin):
    readonly_fields = ["features",
                       "image_render",
                       "isolated_render",
                       ]
    date_hierarchy = 'created_at'
    list_display = ('image_render', 'isolated_render', 'created_at', 'owner')
    fields = ('image_render', 'isolated_render', 'owner')

    def image_render(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=100,
            height=100,
            ))

    def isolated_render(self, obj):
        if not obj.isolated_image:
            return ''
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.isolated_image.url,
            width=100,
            height=100,
            ))


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    readonly_fields = []
    date_hierarchy = 'created_at'
    list_display = ('image_render', 'similarity', 'sock1', 'sock2',)
    fields = ('image_render',)

    def image_render(self, obj):
        return mark_safe('<img src="{url1}" width="{width}" height={height} />\n '
                         '<img src="{url2}" width="{width}" height={height} />'
                         .format(
                            url1=obj.sock1.image.url,
                            url2=obj.sock2.image.url,
                            width=100,
                            height=100,
                          ))
