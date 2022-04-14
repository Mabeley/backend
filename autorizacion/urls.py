from django.urls import path
from .views import RegistroUsuarioApiView

#esto me retornara dos token una de acceso y una de refresh
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns =[
    path('registro/',RegistroUsuarioApiView.as_view()),
    path('inicio-sesion/', TokenObtainPairView.as_view())
]