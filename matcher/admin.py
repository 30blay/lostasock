from django.contrib import admin
from .models import Sock, Match

# Register your models here.

@admin.register(Sock)
class SockAdmin(admin.ModelAdmin):
    readonly_fields = ["features"]


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    readonly_fields = []
    #readonly_fields = ["distance"]
