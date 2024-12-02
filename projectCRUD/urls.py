from django.urls import path
from crud import views

urlpatterns = [
    path('create/', views.create_item, name='create_item'),
    path('read/<int:id>/', views.read_item, name='read_item'),
    path('readall/', views.get_all_items, name='get_all_items'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
