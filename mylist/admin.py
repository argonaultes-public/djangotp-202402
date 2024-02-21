from django.contrib import admin

from .models import ShopList, ShopListItem

# Register your models here.

admin.site.register([ShopList, ShopListItem])