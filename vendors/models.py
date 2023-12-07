from django.db import models
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(
        max_length=100, help_text="Vendor's name")
    contact_details = models.TextField(
        help_text="Contact information of the vendor")
    address = models.TextField(
        help_text="Physical address of the vendor")
    vendor_code = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="A unique identifier for the vendor")
    on_time_delivery_rate = models.FloatField(
        default=0,
        help_text="Tracks the percentage of on-time deliveries")
    quality_rating_avg = models.FloatField(
        default=0,
        help_text="Average rating of quality based on purchase orders")
    average_response_time = models.FloatField(
        default=0,
        help_text="Average time taken to acknowledge purchase orders")
    fulfillment_rate = models.FloatField(
        default=0,
        help_text="Percentage of purchase orders fulfilled successfully")

    def __str__(self):
        return self.name  
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class PurchaseOrder(models.Model):
    PO_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    po_number = models.CharField(
        max_length=10, unique=True, help_text="Unique number identifying the PO")
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, help_text="Link to the Vendor model")
    order_date = models.DateTimeField(
        help_text="Date when the order was placed")
    delivery_date = models.DateTimeField(
        help_text="Expected or actual delivery date of the order")
    items = models.JSONField(
        help_text="Details of items ordered")
    quantity = models.IntegerField(
        help_text="Total quantity of items in the PO")
    status = models.CharField(
        max_length=20, choices=PO_STATUS_CHOICES, help_text="Current status of the PO")
    quality_rating = models.FloatField(
        null=True, blank=True, help_text="Rating given to the vendor for this PO")
    issue_date = models.DateTimeField(
        help_text="Timestamp when the PO was issued to the vendor")
    acknowledgment_date = models.DateTimeField(
        null=True, blank=True, help_text="Timestamp when the vendor acknowledged the PO")

    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}" 

    def acknowledge(self):
        # Update acknowledgment_datetime
        self.acknowledgment_date = timezone.now()
        self.save()

    def calculate_on_time_delivery_rate(self):
        """calculate on-time delivery rate"""
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor, status='completed')
        total_completed_orders = completed_orders.count()
        
        on_time_orders = completed_orders.filter(
            delivery_date__lte=models.F('actual_delivery_date'))
        on_time_count = on_time_orders.count()
            
        if total_completed_orders > 0:
            on_time_delivery_rate = on_time_count / total_completed_orders * 100
            self.vendor.on_time_delivery_rate = on_time_delivery_rate
            self.vendor.save()


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, help_text="Link to the Vendor model")
    date = models.DateTimeField(
        help_text="Date of the performance record")
    on_time_delivery_rate = models.FloatField(
        help_text="Historical record of the on-time delivery rate")
    quality_rating_avg = models.FloatField(
        help_text="Historical record of the quality rating average")
    average_response_time = models.FloatField(
        help_text="Historical record of the average response time")
    fulfillment_rate = models.FloatField(
        help_text="Historical record of the fulfillment rate")

    def __str__(self):
        return f"{self.vendor.name} - Performance on {self.date}" 
