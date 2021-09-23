from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('shows',views.show, name='shows'),
    path('shows/new',views.new, name='new'),
    path('shows/create',views.create, name='create'),
    path('shows/edit',views.edit, name='edit'),
    path('shows/<int:id>',views.show_id, name='show_id'),
    path('shows/<int:id>/edit',views.edit_id, name='edit_id'),
    path('shows/<int:id>/delete',views.delete_id, name='delete_id'),
]