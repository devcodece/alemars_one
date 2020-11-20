from django.db import models

class CdtCategory(models.Model):
    tx_category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tx_category_name


class CdtSubcategory(models.Model):
    tx_subcategory_name = models.CharField(max_length=50)
    id_category = models.ForeignKey(CdtCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.tx_subcategory_name

class CdtBrand(models.Model):
    tx_brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.tx_brand_name

class CdtVendor(models.Model):
    tx_name_vendor = models.CharField(max_length=50)
    nm_phone_number_vendor = models.CharField(max_length=10, blank=True, null=True)
    tx_description = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return self.tx_name_vendor

class CdtColor(models.Model):
    tx_name_color = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
    
    def __str__(self):
        return self.tx_name_color

class CdtSize(models.Model):
    tx_name_size = models.CharField(max_length=4)

    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.tx_name_size

class TdtProduct(models.Model):
    GENDER_CHOICES = [
        ('0', 'Gender'),
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Other'),
    ]

    tx_product_name = models.CharField(max_length=75)
    tx_description = models.CharField(max_length=75)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='0')
    nm_sale_unit = models.DecimalField(max_digits=8, decimal_places=2)
    id_subcategory = models.ForeignKey(CdtSubcategory, on_delete=models.CASCADE)
    id_brand = models.ForeignKey(CdtBrand, on_delete=models.CASCADE)
    id_vendor = models.ForeignKey(CdtVendor, on_delete=models.CASCADE)
    color = models.ForeignKey(CdtColor, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(CdtSize, on_delete=models.CASCADE, blank=True, null=True)
    img_photo1 = models.ImageField(null=True, blank = True)
    img_photo2 = models.ImageField(null=True, blank = True)
    img_photo3 = models.ImageField(null=True, blank = True)
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.tx_product_name

    
""" class CdtProductPhoto(models.Model):
    tx_url_photo = models.ImageField(null=True, blank=True)
    bl_primary = models.BooleanField(default=False)
    id_product = models.ForeignKey(TdtProduct, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    def __str__(self):
        return str(self.tx_url_photo) """