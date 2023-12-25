from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)

from .models import Product, Category
from .forms import ProductForm


def CategoryView(request, cstr):
    """
    Function to display products
    belonging to a specific category
    """
    category = Category.objects.get(name=cstr)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    
    return render(request, "category.html", {"products":products, "category":category, "categories":categories})


class ProductList(generic.ListView):
    """
    ListView to display products
    Paginated list of 10
    """
    model = Product
    paginate_by = 10
    queryset = Product.objects.filter(status=1).order_by('category')
    template_name = 'shop.html'


class ProductDetails(View):
    """
    Product detail view
    Get method to retrieve
    and render details for product
    """
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


class AddProduct(UserPassesTestMixin, generic.CreateView):
    """
    Add product view
    test_func to make sure user is superuser
    """
    template_name = '../templates/add_product.html'
    model = Product
    form_class = ProductForm
    
    success_url = '/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProduct, self).form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser
    

class DeleteProduct(UserPassesTestMixin, generic.DeleteView):
    """
    Delete a product
    test_func to make sure user is superuser
    """
    model = Product
    success_url = '/'
    template_name = 'product_confirm_delete.html'
    
    def test_func(self):
        return self.request.user.is_superuser


class EditProduct(UserPassesTestMixin, generic.UpdateView):
    """
    Update a product
    test_func to make sure user is superuser
    """
    template_name = 'edit_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/'
    
    def test_func(self):
        return self.request.user.is_superuser