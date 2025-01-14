from django.urls import path
from .views.table_view import TableCreateView, TableListView, TableUpdateView,  TableDestroyView
from .views.side_view import  SideCreateView, SideListView, SideUpdateView, SideDestroyView
from .views.addons_views import AddonsCreateView, AddonsListView, AddonsUpdateView, AddonsDestroyView
from .views.order_views import OrderCreateView, OrderUpdateView, OrderListView, OrderListDetails
from .views.item_order_views import ItemOrderCreateView, ItemOrderUpdateView, ItemOrderDestroyView

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

    # Additional Router
    path('create-addons/', AddonsCreateView.as_view(), name = 'create-addons'),
    path('list-addons/', AddonsListView.as_view(), name = 'list-addons'),
    path('<int:pk>/update-addons/', AddonsUpdateView.as_view(), name = 'update-addons'),
    path('<int:pk>/delete-addons/', AddonsDestroyView.as_view(), name = 'delete-addons'),
    
    # Order Router
    path('create-order/', OrderCreateView.as_view(), name = 'create-order'),
    path('<int:id>/update-order/', OrderUpdateView.as_view(), name = 'update-view'),
    path('list-order/', OrderListView.as_view(), name = 'list-order'),
    path('<int:id>/get-order/', OrderListDetails.as_view(), name = 'get-order'),

    # Item Order Router
    path('<int:id>/add-item/', ItemOrderCreateView.as_view(), name = 'add-item'),
    path('<int:id>/update-item-order/', ItemOrderUpdateView.as_view(), name = 'update-item-order'),
    path('<int:pk>/delete-item-order/', ItemOrderDestroyView.as_view(), name='delete-item-order')
]


