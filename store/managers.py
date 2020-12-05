from django.db import models

class ColorManager(models.Manager):
    pass

class CdtProductManager(models.Manager):
    def product_by_color(self, color):
        colors = self.filter(
            tdtproduct_cdtcolor__id__id=color
        )
        return colors