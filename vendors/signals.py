from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Count, Q, Sum

from .models import PurchaseOrder



@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, created, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        vendor = instance.vendor
        
        # Calculate quality rating sum and count of completed orders with ratings
        vendor_stats = PurchaseOrder.objects.filter(
            vendor=vendor, status='completed', quality_rating__isnull=False
        ).aggregate(
            total_rating=Sum('quality_rating'),
            completed_with_rating=Count('id')
        )

        quality_rating_sum = vendor_stats['total_rating']
        total_completed_with_rating = vendor_stats['completed_with_rating']

        if total_completed_with_rating > 0:
            quality_rating_avg = quality_rating_sum / total_completed_with_rating
            # Update vendor's quality_rating_avg field
            vendor.quality_rating_avg=quality_rating_avg
            vendor.save()



@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    if instance.acknowledgment_date is not None:
        vendor = instance.vendor
        
        # Get all POs for the vendor
        vendor_purchases = PurchaseOrder.objects.filter(vendor=vendor)

        # Get all acknowledged POs for the vendor
        acknowledged_orders = vendor_purchases.filter(
            acknowledgment_date__isnull=False)
        
        # Calculate response times in seconds for acknowledged POs
        response_times = [
            (order.acknowledgment_date - order.issue_date).total_seconds()\
                / 3600 for order in acknowledged_orders
        ]

        if len(response_times) > 0:
            average_response_time = sum(response_times) / vendor_purchases.count()
            vendor.average_response_time = average_response_time
            vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, created, **kwargs):
    vendor = instance.vendor

    # Get counts of completed and total POs for the vendor
    vendor_purchases = PurchaseOrder.objects.filter(vendor=vendor)
    purchase_counts = vendor_purchases.aggregate(
        total_count=Count('id'),
        fulfilled_count=Count('id', filter=Q(status='completed'))
    )

    total_orders = purchase_counts['total_count']
    fulfilled_orders = purchase_counts['fulfilled_count']

    if vendor_purchases:
        fulfillment_rate = fulfilled_orders / total_orders
        vendor.fulfillment_rate = fulfillment_rate
        vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def calculate_on_time_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor
        completed_orders = PurchaseOrder.objects.filter(
            vendor=vendor, status='completed')
        total_completed_orders = completed_orders.count()

        on_time_orders = completed_orders.filter(
            delivery_date__lte=instance.delivery_date)
        on_time_count = on_time_orders.count()

        if total_completed_orders > 0:
            on_time_delivery_rate = (on_time_count / total_completed_orders) * 100
            vendor.on_time_delivery_rate = on_time_delivery_rate
            vendor.save()