from django.urls import path

from eln.views.PersonVial import PersonVialView
from eln.views.ProductAnalytic import ProductAnalyticView
from eln.views.VialSampleCreation import VialSampleCreateView
from eln.views.VialSplittingCreation import VialSplittingCreateView

urlpatterns = [
    path('api/product-analytics/', ProductAnalyticView.as_view(), name='product-analytics'),
    path('api/samples/<int:sample_id>/vials/', VialSampleCreateView.as_view(), name='vial-sample-create'),
    path('api/vials/<int:vial_id>/split/', VialSplittingCreateView.as_view(), name='vial-split-create'),
    path('person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
]
