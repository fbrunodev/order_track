from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import LoginView,UserView





urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    # Urls do login
    path('login/', LoginView.as_view(),name='login'),
    # Urls user
    path('user/', UserView.as_view(), name='user' )

]
