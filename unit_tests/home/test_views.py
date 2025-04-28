from django.urls import reverse 
from django.test import Client
from pytest_django.asserts import assertTemplateUsed
import pytest

from home.views import RedirectHomeView, HomeView
from products.models import Product


def test_RedirectHomeView():
    client = Client()
    response = client.get(reverse('redirect_home'))

    """ 
    Testing if our RedirectHomeView redirects succuessfully (status_code 302)
    For the second assert, We are testing if we redirect to the '/home/' url
     """

    assert response.status_code == 302
    assert response.url == '/home/'

@pytest.mark.django_db
def test_HomeView():
    client = Client()
    response = client.get(reverse('home'))

    """ 
    In the first assert, We are testing if our get request returns 200 (OK) status code 
    For the second assert, we are making sure that our view returns the home.html template
    """
    
    assert response.status_code == 200
    assertTemplateUsed(response, 'home.html')

@pytest.mark.django_db
def test_homeview_price_filter():
    # Création de produits avec des prix différents
    Product.objects.create(name="Produit 1", image="test.jpg", description="test", price=10.00)
    Product.objects.create(name="Produit 2", image="test.jpg", description="test", price=50.00)
    Product.objects.create(name="Produit 3", image="test.jpg", description="test", price=100.00)

    client = Client()

    # Requête avec filtre de prix
    response = client.get(reverse('home') + '?min_price=20&max_price=80')

    # On s'assure que la requête s'est bien passée
    assert response.status_code == 200

    # On vérifie que le bon produit est présent
    content = response.content.decode()
    assert "Produit 2" in content
    assert "Produit 1" not in content
    assert "Produit 3" not in content
