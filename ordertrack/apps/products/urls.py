from django.urls import path

from .views import ProductListView,ProductCreateView, ProductUpdateView, ProductDestroyView
from.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDestroyView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create-product'),
    path('', ProductListView.as_view(), name='list-products'),
    path('update/<int:pk>/',ProductUpdateView.as_view() , name='update-product'),
    path('<int:pk>/delete/', ProductDestroyView.as_view(), name='delete-product'),

    # routers related category
    path('list-category/', CategoryListView.as_view(), name='list-category'),
    path('create-category/', CategoryCreateView.as_view(), name='create-category'),
    path('<int:pk>/update-category/', CategoryUpdateView.as_view(), name='update-category'),
    path('<int:pk>/delete-category/', CategoryDestroyView.as_view(), name='delete-category')

]