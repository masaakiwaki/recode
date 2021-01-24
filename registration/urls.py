from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.PersonCreateView.as_view(), name='person_test'),
    path('list/', views.PersonListView.as_view(), name='person_list'),
    path('detail/<int:pk>/', views.PersonDetailView.as_view(), name='person_detail'),
    path('update/<int:pk>/', views.PersonUpdateView.as_view(), name='person_update'),
    path('delete/<int:pk>/', views.PersonDeleteView.as_view(), name='person_delete'),
    path('family/<int:pk>/result/', views.ResultListView.as_view(), name='result_list'),
    path('family/<int:pk>/create/', views.ResultCreateView.as_view(), name='result_create'),
    path('family/<int:pk>/update/', views.ResultUpdateView.as_view(), name='result_update'),
    path('family/<int:pk>/delete/', views.ResultDeleteView.as_view(), name='result_delete'),
]