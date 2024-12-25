from django.urls import path

from eln.views.PersonVial import PersonVialView
from eln.views.ProductAnalytic import ProductAnalyticView

urlpatterns = [
    path('api/product-analytics/', ProductAnalyticView.as_view(), name='product-analytics'),
    path('person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
]
