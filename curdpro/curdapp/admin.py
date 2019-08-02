from django.contrib import admin
from curdapp.models import ProductData


class ProductDataAdmin(admin.ModelAdmin):

    list_display = ['product_number','product_name','product_cost','product_class','product_weight']
admin.site.register(ProductData,ProductDataAdmin)