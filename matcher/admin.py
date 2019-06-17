from django.contrib import admin
from .models import Sock, Match

admin.site.site_header = 'Lostasock Administration'
admin.site.site_title = admin.site.site_header
admin.site.index_title = 'Home'

# Register your models here.
@admin.register(Sock)
class SockAdmin(admin.ModelAdmin):
    readonly_fields = ["features"]
    date_hierarchy = 'created_at'
    list_display = ('created_at', 'owner')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    readonly_fields = []
    date_hierarchy = 'created_at'
    list_display = ('similarity', 'sock1', 'sock2')

