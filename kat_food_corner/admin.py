from django.contrib import admin

from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name",)
    ordering = ("name",)
