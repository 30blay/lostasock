from django.contrib import admin
from .models import Sock

# Register your models here.

@admin.register(Sock)
class SockAdmin(admin.ModelAdmin):
    readonly_fields = ["features"]