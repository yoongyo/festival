from django.contrib import admin
from .models import Festival, FestivalImage, FestivalComment, FestivalSNS, FestivalArea


class FestivalAdmin(admin.ModelAdmin):
    list_display = ['name']


class FestivalImageAdmin(admin.ModelAdmin):
    list_display = ['festival']


class FestivalCommentAdmin(admin.ModelAdmin):
    list_display = ['festival', 'comment']


class FestivalSNSAdmin(admin.ModelAdmin):
    list_display = ['festival']


class FestivalAreaAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Festival, FestivalAdmin)
admin.site.register(FestivalImage, FestivalImageAdmin)
admin.site.register(FestivalComment, FestivalCommentAdmin)
admin.site.register(FestivalArea, FestivalAreaAdmin)
admin.site.register(FestivalSNS, FestivalSNSAdmin)
