from django.urls import path
from .views import DisheApiView, DisheListView, DishUpdateView, DisheDestroyView

urlpatterns = [
    path('create/',DisheApiView.as_view(), name= 'create'),
    path('list/', DisheListView.as_view(), name = 'list'),
    path('<int:pk>/update/', DishUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', DisheDestroyView.as_view(), name='delete'),
]