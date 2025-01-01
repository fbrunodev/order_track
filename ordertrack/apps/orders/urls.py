from django.urls import path
from .views.table_view import TableCreateView, TableListView, TableUpdateView,  TableDestroyView
from .views.side_view import  SideCreateView, SideListView, SideUpdateView, SideDestroyView
urlpatterns = [
    # Tables router
    path('create-table/',TableCreateView.as_view(), name="create-table"),
    path('list-table/', TableListView.as_view(), name = 'list-table'),
    path('<int:pk>/update-table/', TableUpdateView.as_view(), name = 'update-table'),
    path('<int:pk>/delete-table/', TableDestroyView.as_view(), name = 'delete-table'),

    # Sides Router
    path('create-side/', SideCreateView.as_view(), name = 'create-side'),
    path('list-side/', SideListView.as_view(), name = 'list-side'),
    path('<int:pk>/update-side/', SideUpdateView.as_view(), name ='update-side'),
    path('<int:pk>/delete-side/', SideDestroyView.as_view(), name = 'delete-side'),
]