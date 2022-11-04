
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='list'),
    path('random/', views.randomProjects, name='random'),
    path('<int:pk>/', views.RetriveProjectAPIView.as_view(), name='retrive'),
    path('create/', views.ProjectListCreateAPIView.as_view(), name='create'),
    path('add/', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>/', views.project_detail, name='detail')
]
