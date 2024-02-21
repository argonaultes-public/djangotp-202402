from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_gt_0(value):
    if value <= 0:
        raise ValidationError(
            _("%(value)s is not greater than 0"),
            params={"value": value},
        )


class ShopList(models.Model):
    name = models.CharField(max_length=200)

    @property
    def nb_items(self):
        return self.shoplistitem_set.count()

    def __str__(self):
        return self.name

class ShopListItem(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(validators = [validate_gt_0])
    shop_list = models.ForeignKey(ShopList, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ({self.quantity}) in {self.shop_list.name}'
