from django.urls import path
from .views import PersonCreateView,  PersonListView, PersonDetailView, PersonUpdateView, PersonDeleteView
 
urlpatterns = [
    path('', PersonCreateView.as_view()),
    path('list/', PersonListView.as_view(), name='person_list'),
    path('<int:pk>/detail', PersonDetailView.as_view(), name='person_detail'),
    path('<int:pk>/update/', PersonUpdateView.as_view(), name='person_update'),
    path('<int:pk>/delete/', PersonDeleteView.as_view(), name='person_delete'),
]