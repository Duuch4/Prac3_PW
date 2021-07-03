from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView
from era.models import Facultad
from era.views import *

'''
from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView
'''
app_name = "era"

urlpatterns = [
    path('', ListView.as_view(queryset=Facultad.objects.order_by('-name'),
                              context_object_name='facultad_list',
                              template_name='era/facultadList.html'),
         name='facultad_list'),

    path('facultad/create',
         FacultadCreate.as_view(),
         name='create_facultad'),

    path('facultad/<int:pk>',
         FaculdadDetails.as_view(),
         name='facultad_details'),

    path('facultad/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Facultad,
             form_class=FacultadForm
         ),
         name='facultad_edit'),

    path('facultad/<int:pk>/delete',
         FacultadDelete.as_view(),
         name='facultad_delete'),

    path('facultad/<int:pk>/career/create/',
         CareerCreate.as_view(),
         name='create_career'),

    path('facultad/<int:pkr>/career/<int:pk>',
         CareerDetails.as_view(),
         name='career_details'),

    path('facultad/<int:pkr>/career/<int:pk>/edit',
         LoginRequiredCheckIsOwnerUpdateView.as_view(
             model=Carrera,
             form_class=CarrerForm
         ),
         name='career_edit'),

    path('facultad/<int:pkr>/career/<int:pk>/delete',
         CareerDelete.as_view(),
         name='career_delete'),
]
