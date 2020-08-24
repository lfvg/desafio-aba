from django.urls import include, path
from rest_framework import routers
from myproject.core import views as v
from . import views

app_name = 'core'


router = routers.DefaultRouter()
router.register('user', v.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:user_id>', views.user, name='user'),
    path('users', views.getUsers, name='getUsers'),
    path('create/user/', views.createUser, name='createUser'),
    path('create/user', views.createUser, name='createUser'),
    path('departamentos', views.getDepartamentos, name='getDepartamentos'),
]
