from django.urls import path

from .views import edit,update,delete,add,create,index

urlpatterns = [
    path('', index, name='index' ),
    path('create/', create, name='create'),
    path('add/', add, name='add'),
    path('delete/<id>/', delete, name='delete'),
    path('edit/<id>/', edit, name='edit'),
    path('update/<id>/', update, name='update'),

]
