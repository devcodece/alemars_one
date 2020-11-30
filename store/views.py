from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from . models import TdtProduct, CdtColor
from . forms import TdtProductForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'home.html')

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

