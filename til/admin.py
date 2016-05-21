from django.contrib import admin

from .models import TIL


class TilAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'private', 'user')

admin.site.register(TIL, TilAdmin)
