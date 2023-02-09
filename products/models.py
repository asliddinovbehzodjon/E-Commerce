from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
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
class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=400,verbose_name=_("Product name"))
    image = models.ImageField(upload_to="product-images",verbose_name=_("Product image"))
    category = models.ManyToManyField(Category,related_name='products',verbose_name=_("Choose category"))
    description = models.TextField(verbose_name=_("Product description"))
    price = models.IntegerField(verbose_name=_("Product price"))
    discount = models.IntegerField(verbose_name=_("Product discount"),default=0)
    def __str__(self):
        return self.name
    class Meta:
        db_table ="Product"
        verbose_name = _("Product ")
        verbose_name_plural= _("Products ")
    @property
    def picture(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
class Album(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='rasmlar')
    image = models.ImageField(upload_to='product-albums')
    def __str__(self):
        return self.product.name
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    @property
    def all_products(self):
        paketlar = self.paket.all()
        return sum([i.quantity for i in paketlar])
    @property
    def all_mahsulot(self):
        paketlar  = self.paket.all()
        return [i.mahsulot for i in paketlar]
    @property
    def all_price(self):
        paketlar = self.paket.all()
        return sum([i.xarid for i in paketlar])

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='paket')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.order} ning xaridi!"
    @property
    def mahsulot(self):
        return self.product
    @property
    def narx(self):
        return self.product.price
    @property
    def xarid(self):
        return self.product.price *self.quantity




