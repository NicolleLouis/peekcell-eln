from django.urls import path

from eln.views.PersonVial import PersonVialView
from eln.views.ProductAnalytic import ProductAnalyticView
from eln.views.VialBatchCreation import VialBatchCreateView

urlpatterns = [
    path('api/product-analytics/', ProductAnalyticView.as_view(), name='product-analytics'),
    path('api/samples/<int:sample_id>/vials/', VialBatchCreateView.as_view(), name='vial-batch-create'),
    path('person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
]
