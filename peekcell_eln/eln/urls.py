from django.urls import path

from eln.views.PersonVial import PersonVialView

urlpatterns = [
    path('person/<int:pk>/vials/', PersonVialView.as_view(), name='person-vials'),
]
