from django.urls import path

from eln.views.api.PersonVial import PersonVialView
from eln.views.api.ProductAnalytic import ProductAnalyticView
from eln.views.api.VialSampleCreation import VialSampleCreateView
from eln.views.api.VialSplittingCreation import VialSplittingCreateView

urlpatterns = [
    path('api/product-analytics/', ProductAnalyticView.as_view(), name='product-analytics'),
    path('api/samples/<int:sample_id>/vials/', VialSampleCreateView.as_view(), name='vial-sample-create'),
    path('api/vials/<int:vial_id>/split/', VialSplittingCreateView.as_view(), name='vial-split-create'),
    path('person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
]
