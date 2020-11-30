from django.contrib import admin
from . models import (
    CdtCategoryPerson,
    CdtCategory,
    CdtSubcategory,
    CdtBrand,
    CdtVendor,
    CdtColor,
    CdtProductPhoto,
    TdtProduct,
    CdtSize,
    TdtSkuProduct,
    )

class CdtCategoryPersonAdmin(admin.ModelAdmin):
    list_display = ('tx_category_person',)

class CdtCategoryAdmin(admin.ModelAdmin):
    list_display = ('tx_category_name',)

class CdtSubcategoryAdmin(admin.ModelAdmin):
    list_display = ('tx_subcategory_name',)

class CdtBrandAdmin(admin.ModelAdmin):
    list_display = ('tx_brand_name',)

class CdtVendorAdmin(admin.ModelAdmin):
    list_display = ('tx_name_vendor',)

class CdtColorAdmin(admin.ModelAdmin):
    list_display = ('tx_name_color',)

class CdtProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tx_url_photo',)

class TdtProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'tx_product_name',)

class CdtSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

class TdtSkuProductAdmin(admin.ModelAdmin):
    list_display = ('sku',)

""" class CdtSizeAdmin(admin.ModelAdmin):
    list_display = ('tx_name_size',) """



admin.site.register(CdtCategoryPerson, CdtCategoryPersonAdmin)
admin.site.register(CdtCategory, CdtCategoryAdmin)
admin.site.register(CdtSubcategory, CdtSubcategoryAdmin)
admin.site.register(CdtBrand, CdtBrandAdmin)
admin.site.register(CdtVendor, CdtVendorAdmin)
admin.site.register(CdtColor, CdtColorAdmin)
admin.site.register(CdtProductPhoto, CdtProductPhotoAdmin)
#admin.site.register(CdtSize, CdtSizeAdmin)
admin.site.register(TdtProduct, TdtProductAdmin)
admin.site.register(CdtSize, CdtSizeAdmin)
admin.site.register(TdtSkuProduct, TdtSkuProductAdmin)

