from django.urls import path
from .views import GenerarComprobanteApiView

urlpatterns =[
    path('generar_comprobante/', GenerarComprobanteApiView.as_view(),
    
    )
]