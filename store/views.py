from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormView

from . models import (CdtCategoryPerson, CdtCategory, CdtSubcategory,
CdtBrand, CdtVendor, CdtColor, CdtProductPhoto, TdtProduct, CdtSize,
TdtSkuProduct)

from . forms import TdtProductForm, NewProductForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new_product(request):
    return render(request, 'new-product.html')

class CrudProduct(ListView):
    model = TdtProduct
    #model_two = CdtColor
    template_name = 'crud-product.html'
    paginate_by = 6
    context_object_name = 'products'
    form_class = TdtProductForm

    
#class CrudProduct(ListView):
    #model = TdtProduct
    #template_name = 'crud-product.html'
    #paginate_by = 3
    #form_class = TdtProductForm
    #context_object_name = 'products'

    #Retorna consulta de todos los productos
    #def get_queryset(self):
    #    return self.    .all()
        
    #Asignar a get_queryset el context products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['color'] = CdtColor.objects.all()
        #print(color + '===================')
        return context

class NewProduct(FormView):
    template_name = 'crud-product/create.html'
    form_class = NewProductForm
    success_url = 'crud-product.html'

    def form_valid(self, form):
        #instance CategoryPerson
        category_person = CdtCategoryPerson.objects.all()
        #category_person = CdtCategoryPerson(
            #tx_category_person = form.cleaned_data['idcat_person'],
        #)
        #category_person.save()
        #instance Category
        category = CdtCategory(
            tx_category_name = form.cleaned_data['idcat'],
            id_category_person = category_person,
        )
        category.save()
        #instance SubCategory
        subcategory = CdtSubcategory(
            tx_subcategory_name = form.cleaned_data['idsubcat'],
            id_category = category,
        )
        subcategory.save()
        #instance Brand
        brand = CdtBrand(
            tx_brand_name = form.cleaned_data['brand'],
        )
        brand.save()
        #instance Vendor
        vendor = CdtVendor(
            tx_name_vendor = form.cleaned_data['idvendor'],
        )
        vendor.save()
        #instance Color
        color = CdtColor(
            tx_name_color = form.cleaned_data['idcolor'],
        )
        color.save()
        #instance Photo
        photo = CdtProductPhoto(
            tx_url_photo = form.cleaned_data['idphoto'],
            bl_primary = form.cleaned_data['primary']
        )
        photo.save()

        name = form.cleaned_data['name']
        description = form.cleaned_data['description']

        TdtProduct.objects.create(
            tx_product_name = name,
            tx_description = description,
            id_category_person = category_person,
            id_category = category,
            id_subcategory = subcategory,
            id_brand = brand,
            id_vendor = vendor,
            id_color = color,
            id_photo = photo,
        )
        return super(NewProduct, self).form_valid(form)





    #Renderizando el template y pasando el context
    #def get(self, request, *args, **kwargs):
        #return render(request, self.template_name, self.get_context_data())
    
    #def pagination(request):
        #product_list = self.get_queryset()
        #paginator = Paginator(product_list, 3)
        #page = request.GET.get('page')
        #product_list = paginator.get_page(page)

        #return render(request, self.template_name, self.get_context_data(), {'products':product_list})

    #def get(self, request, *args, **kwargs):
        #product_list = self.get_queryset()
        
        #print(product_list)
        #paginator = Paginator(product_list,3)
        
        #page = request.GET.get('page')
        #print(page)
        #products = paginator.get_page(page)
        #print(products)
        #return render(request, self.template_name, self.get_context_data(), {'products':products})

    


    #Guardando los datos del formulario con el metodo post
    #def post(self, request, *args, **kwargs):
    #    form = self.form_class(request.POST)
    #    if form.is_valid:
    #        form.save()
    #        return redirect('crud-product')
    
    #Paginacion
    #def pagination(request):
        #product_list = self.get_context_data()
        #paginator = Paginator(product_list, 3)

        #page_number = request.GET.get('page')
        #product_list = paginator.get_page(page_number) 
        #return render(request, self.template_name, {'page_obj':page_obj})


class UpdateProduct(UpdateView):
    model = TdtProduct
    template_name = 'update.html'
    form_class = TdtProductForm
    success_url = reverse_lazy('crud-product')

    #Guardando los datos del formulario con el metodo post
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['form'] = self.form_class
        #context['object'] = self.get_object()
        #return context


class CreateProduct(CreateView):
    model = TdtProduct
    template_name = 'create.html'
    form_class = TdtProductForm
    success_url = reverse_lazy('crud-product')


class DeleteProduct(DeleteView):
    model = TdtProduct
    success_url = reverse_lazy('crud-product')


class ProductCatalogList(ListView):

    model = TdtProduct
    template_name = 'catalog-page.html'
    context_object_name = 'products'

