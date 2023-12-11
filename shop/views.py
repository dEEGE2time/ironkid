from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View

from django.contrib.auth.mixins import LoginRequiredMixin

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
        comments = product.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            'product_detail.html',
            {
                'product': product,
                'comments': comments, 
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
    
    