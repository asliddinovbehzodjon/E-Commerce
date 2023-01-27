from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
class Category(models.Model):
    name = models.CharField(max_length=150,verbose_name=_("Category name"),null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Category"
        verbose_name = _("Category ")
        verbose_name_plural = _("Categories ")

