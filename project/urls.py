"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from car import api
from accounts import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [   
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('api/cars', api.car_list_api, name='car_list'),
    path('api/cars/<int:id>',api.car_details_api,name='car_details'),
    path('api/cars/new',api.new_car,name='new_car'),
    path('api/cars/update/<int:id>',api.update_car,name='update_car'),
    path('api/cars/delete/<int:id>',api.delete_car,name='delete_car'),

    

    path('api/register', views.register_user, name='register'),
    

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('userinfo', views.current_user, name='user_info'),

]


