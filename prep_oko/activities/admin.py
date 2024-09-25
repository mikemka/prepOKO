from django.contrib import admin
from . import models


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LevelType)
class LevelTypeAdmin(admin.ModelAdmin):
    pass
