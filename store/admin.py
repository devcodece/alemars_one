from django.contrib import admin
from . models import (
    CdtCategory,
    CdtSubcategory,
    CdtBrand,
    CdtVendor,
    CdtColor,
    CdtSize,
    TdtProduct)


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

class CdtSizeAdmin(admin.ModelAdmin):
    list_display = ('tx_name_size',)

class TdtProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'tx_product_name',)

admin.site.register(CdtCategory, CdtCategoryAdmin)
admin.site.register(CdtSubcategory, CdtSubcategoryAdmin)
admin.site.register(CdtBrand, CdtBrandAdmin)
admin.site.register(CdtVendor, CdtVendorAdmin)
admin.site.register(CdtColor, CdtColorAdmin)
admin.site.register(CdtSize, CdtSizeAdmin)
admin.site.register(TdtProduct, TdtProductAdmin)