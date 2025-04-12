from django.urls import path
from .views import UpdateBillView, DestroyBillView,ListAllBillView

urlpatterns = [
    # Bill router
    path('list/', ListAllBillView.as_view(), name='list'),
    path('<int:id>/update/', UpdateBillView.as_view(), name = 'update'),
    path('<int:pk>/delete/', DestroyBillView.as_view(), name = 'delete'),
]