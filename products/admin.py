from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['name','user']
    list_per_page = 10
    search_fields = ['name','user']
    fields = ['name']
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True
    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user:
            return False
        return True
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
