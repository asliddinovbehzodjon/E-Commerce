from .models import *
from modeltranslation.translator import TranslationOptions,register
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ("name",'description')