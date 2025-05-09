from django.shortcuts import redirect
from django.views.generic import ListView

from products.models import Product


def RedirectHomeView(request):
    '''
    Redirect url from '/' to '/home/'
    '''
    return redirect('home')

class HomeView(ListView):
    '''
    Renders home page with all the products
    '''
    template_name = 'home.html'
    model = Product
    context_object_name = 'object_list'

    def get_queryset(self):
        """
        Ajout de la features filter by price
        """
        queryset = Product.objects.all()
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset