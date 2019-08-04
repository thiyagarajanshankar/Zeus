from django.contrib import admin

# Register your models here.
from .models import Question

admin.site.register(Question)

admin.site.site_header = "ZEUS Data Management Studio";
admin.site.site_title = "My Product Inventory ";

class ProductAdmin(Question):
    pass

