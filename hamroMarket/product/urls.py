from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('show/', views.show),
    path('product/', views.product),
    path('delete/<int:id>', views.destroy),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('raw_sql/', views.raw_sql),

]
