from django.contrib import admin 
from django.urls import path, include  
from rest_framework.routers import DefaultRouter
from restaurant import views
 
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)  # Agrega la vista de reservas

urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('restaurant/', include('restaurant.urls')),  # Mantén esto para las vistas normales
    path('restaurant/booking/', include(router.urls)),  # Agrega el router aquí
]
