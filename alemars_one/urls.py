"""alemars_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store.views import home, ProductCatalogListView, CreateProduct, CrudProduct, UpdateProduct, DeleteProduct
# 
#step_two, catalog_page,


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('catalog-page/', ProductCatalogListView.as_view(), name = 'catalog-page'),
    
    path('create', CreateProduct.as_view(), name = 'create'),
    path('crud-product',CrudProduct.as_view(),name='crud-product'),
    path('edit-product/<int:pk>',UpdateProduct.as_view(), name='edit-product'),
    path('delete/<int:pk>',DeleteProduct.as_view(), name='delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
