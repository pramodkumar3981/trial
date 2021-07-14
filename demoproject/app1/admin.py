from django.contrib import admin
from .models import Category, Product, Newsletter, Profileusers,Contact,Gender


admin.site.site_header = "My Admin"

# ADMIN CLASSES
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "category_pic")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_desc", "product_pic", "product_view", "product_price", "product_for")
    search_fields=("product_name","product_price","product_for")

class NewsletterAdmin(admin.ModelAdmin):
    list_display=['mailid']

class GenderAdmin(admin.ModelAdmin):
    pass

class ProfileuserAdmin(admin.ModelAdmin):
    list_display=('user','phone','gender','city','doc')

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','subject','message')


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Profileusers,ProfileuserAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Gender,GenderAdmin)

