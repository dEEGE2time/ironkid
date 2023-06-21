from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product

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
        bookmarked = False
        if product.bookmarks.filter(id=self.request.user.id).exists():
            bookmarked = True

        return render(
            request,
            'product_detail.html',
            {
                'product': product,
                'comments': comments,
                'bookmarked': bookmarked   
            },
        )