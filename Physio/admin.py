from django.contrib import admin
from .models import Event, EventImage, Service


class EventImageInline(admin.TabularInline):
    model = EventImage


class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    list_display = ('event_name', 'event_cover', 'date', 'details')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Event, EventAdmin)
admin.site.register(Service, ServiceAdmin)