from django.urls import path
from . import views

app_name = 'vendors'

urlpatterns = [
    path('vendors/', views.VendorList.as_view(), name='vendors'),
    path('vendors/<int:pk>/', views.VendorDetail.as_view(), name='vendor-detail'),
    path('purchase_orders/', views.PurchaseOrderListCreateAPIView.as_view()),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderDetailAPIView.as_view()),
    path('vendors/<int:vendor_id>/performance/', views.VendorPerformanceAPIView.as_view()),
    path('purchase_orders/<int:po_id>/acknowledge/', views.AcknowledgePurchaseOrderAPIView.as_view()),
]
