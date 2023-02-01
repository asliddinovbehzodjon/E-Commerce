from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
class AlbumInline(admin.TabularInline):
    model = Album
# Register your models here.
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
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
def discount_50(modeladmin, request, queryset):
    for i in queryset:
        i.discount = i.price - i.price * 0.5
        i.price = i.price*0.5
        i.save()
def discount_90(modeladmin, request, queryset):
    for i in queryset:
        i.discount = i.price - i.price*0.1
        i.price = i.price*0.1
        i.save()
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display =  ['picture','name','user','price','discount']
    list_per_page = 10
    search_fields = ['name','user','price','description','discount']
    fields = ['name','image','category','description','price','discount']
    actions = [discount_50,discount_90]
    inlines = [AlbumInline]
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
@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ['product','quantity','narx','xarid']
    list_editable = ['quantity']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','all_products','all_price']