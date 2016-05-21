from django.contrib import admin

from .models import Peak


class PeakAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'private', 'user')

admin.site.register(Peak, PeakAdmin)
