from django.contrib import admin
from . models import (
    CdtCategory,
    CdtSubcategory,
    CdtBrand,
    CdtVendor,
    CdtColor,
    TdtProduct,
    CdtProductPhoto,
    )


class CdtCategoryAdmin(admin.ModelAdmin):
    list_display = ('tx_category_name',)

class CdtSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('tx_subcategory_name',)

class CdtBrandAdmin(admin.ModelAdmin):
    list_display = ('tx_brand_name',)

class CdtVendorAdmin(admin.ModelAdmin):
    list_display = ('tx_name_vendor',)

class TdtProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'tx_product_name',)

class CdtColorAdmin(admin.ModelAdmin):
    list_display = ('tx_name_color',)

class CdtProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('tx_url_photo',)

""" class CdtSizeAdmin(admin.ModelAdmin):
    list_display = ('tx_name_size',) """



admin.site.register(CdtCategory, CdtCategoryAdmin)
admin.site.register(CdtSubcategory, CdtSubcategoryAdmin)
admin.site.register(CdtBrand, CdtBrandAdmin)
admin.site.register(CdtVendor, CdtVendorAdmin)
#admin.site.register(CdtSize, CdtSizeAdmin)
admin.site.register(TdtProduct, TdtProductAdmin)
admin.site.register(CdtColor, CdtColorAdmin)
admin.site.register(CdtProductPhoto, CdtProductPhotoAdmin)