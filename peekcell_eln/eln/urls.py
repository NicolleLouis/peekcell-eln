from django.urls import path

from eln.views.api.experiment import ExperimentView
from eln.views.api.experiment_detail import ExperimentDetailView
from eln.views.api.person_vial import PersonVialView
from eln.views.api.product_analytic import ProductAnalyticView
from eln.views.api.vial_sample_creation import VialSampleCreateView
from eln.views.api.vial_splitting_creation import VialSplittingCreateView
from eln.views.front.experiment_list import ExperimentList
from eln.views.front.home import home
from eln.views.front.product_analytics import ProductAnalyticsView
from eln.views.front.sample_list import SampleList
from eln.views.front.sample_details import sample_details
from eln.views.front.vial_details import vial_details
from eln.views.front.vial_sample_creation import vial_sample_creation

urlpatterns = [
    path('', home, name='home'),
    path('api/experiments/', ExperimentView.as_view(), name='experiments'),
    path('api/experiments/<int:experiment_id>/', ExperimentDetailView.as_view(), name='experiment-detail'),
    path('api/person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
    path('api/product-analytics/', ProductAnalyticView.as_view(), name='api/product-analytics'),
    path('api/samples/<int:sample_id>/vials/', VialSampleCreateView.as_view(), name='vial-sample-create'),
    path('api/vials/<int:vial_id>/split/', VialSplittingCreateView.as_view(), name='vial-split-create'),
    path('experiments/', ExperimentList.as_view(), name='experiments'),
    path('product-analytics/', ProductAnalyticsView.as_view(), name='product-analytics'),
    path('samples/', SampleList.as_view(), name='samples'),
    path('samples/<int:sample_id>/', sample_details, name="sample_details"),
    path('vials/<int:vial_id>/', vial_details, name="vial_details"),
    path('samples/<int:sample_id>/vials/create/', vial_sample_creation, name="vial_sample_creation"),
]
