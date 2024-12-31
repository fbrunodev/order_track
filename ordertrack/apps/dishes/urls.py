from django.urls import path
from .views import DisheApiView, DisheListView, DishUpdateView, DisheDestroyView
from .views import ItemDisheCreateView, ItemDisheListView, ItemDisheUpdateView, ItemDisheDestroyView

urlpatterns = [
    # path for Dishes
    path('create/',DisheApiView.as_view(), name= 'create'),
    path('list/', DisheListView.as_view(), name = 'list'),
    path('<int:pk>/update/', DishUpdateView.as_view(), name = 'update'),
    path('<int:pk>/delete/', DisheDestroyView.as_view(), name='delete'),

    # path for ItemDishes
    path('create-item-dishe/', ItemDisheCreateView.as_view(), name='create-item-dishe'),
    path('list-item-dishe/', ItemDisheListView.as_view(), name='list-item-dishe'),
    path('<int:pk>/item-dishe-update/', ItemDisheUpdateView.as_view(), name = 'item-dishe-update'),
    path('<int:pk>/item-dishe-delete/', ItemDisheDestroyView.as_view(), name ='item-dishe-delete')
]