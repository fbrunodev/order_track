from django.urls import path
from . import views
from .views import TableCreateView, TableListView, TableUpdateView,  TableDestroyView

urlpatterns = [
    # Tables router
    path('create-table/',TableCreateView.as_view(), name="create-table"),
    path('list-table/', TableListView.as_view(), name = 'list-table'),
    path('<int:pk>/update-table/', TableUpdateView.as_view(), name = 'update-table'),
    path('<int:pk>/delete-table/', TableDestroyView.as_view(), name = 'delete-table')
]