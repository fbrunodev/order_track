from django.urls import path

from .views import ProductListView,ProductCreateView, ProductUpdateView, ProductDestroyView

urlpatterns = [
    path('list-products/', ProductListView.as_view(), name='list-products'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/',ProductUpdateView.as_view() , name='update'),
    path('<int:pk>/delete/', ProductDestroyView.as_view(), name='delete')
]