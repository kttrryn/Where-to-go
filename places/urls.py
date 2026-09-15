from django.urls import path
from places import views

app_name = 'places'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('list/', views.places_list_view, name='places_list'),
    path('add/', views.add_place_view, name='add_place'),
    # Детальна сторінка конкретного місця (передаємо id або індекс у списку)
    path('<int:place_id>/', views.place_detail_view, name='place_detail'),
]