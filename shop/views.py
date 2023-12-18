from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Product
from .forms import ProductForm


class ProductList(generic.ListView):
    model = Product
    paginate_by = 10
    queryset = Product.objects.filter(status=1).order_by('category')
    template_name = 'shop.html'


class ProductDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Product.objects.filter(status=1)
        product = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'product_detail.html',
            {
                'product': product,
            },
        )


class AddProduct(LoginRequiredMixin, generic.CreateView):
    """
    Add product view
    """
    template_name = '../templates/add_product.html'
    model = Product
    form_class = ProductForm
    
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)
    

class DeleteProduct(generic.DeleteView):
    """
    Delete a product
    """
    model = Product
    success_url = '/'
    template_name = 'product_confirm_delete.html'


class EditProduct(generic.UpdateView):
    """
    Update a product
    """
    template_name = 'edit_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/'