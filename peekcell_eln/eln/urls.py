from django.urls import path

from eln.views.api.experiment import ExperimentView
from eln.views.api.person_vial import PersonVialView
from eln.views.api.product_analytic import ProductAnalyticView
from eln.views.api.vial_sample_creation import VialSampleCreateView
from eln.views.api.vial_splitting_creation import VialSplittingCreateView
from eln.views.front.experiment_list import ExperimentList
from eln.views.front.product_analytics import ProductAnalyticsView

urlpatterns = [
    path('api/experiments/', ExperimentView.as_view(), name='experiments'),
    path('api/person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
    path('api/product-analytics/', ProductAnalyticView.as_view(), name='api/product-analytics'),
    path('api/samples/<int:sample_id>/vials/', VialSampleCreateView.as_view(), name='vial-sample-create'),
    path('api/vials/<int:vial_id>/split/', VialSplittingCreateView.as_view(), name='vial-split-create'),
    path('product-analytics/', ProductAnalyticsView.as_view(), name='product-analytics'),
    path("experiments/", ExperimentList.as_view())
]
