from django.contrib import admin

from .models import Event


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    """Register Event model in the Admin page."""

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Event, EventAdmin)
