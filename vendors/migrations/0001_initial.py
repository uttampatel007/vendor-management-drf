# Generated by Django 4.2 on 2023-12-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Vendor's name", max_length=100)),
                ('contact_details', models.TextField(help_text='Contact information of the vendor')),
                ('address', models.TextField(help_text='Physical address of the vendor')),
                ('vendor_code', models.CharField(help_text='A unique identifier for the vendor', max_length=50, unique=True)),
                ('on_time_delivery_rate', models.FloatField(help_text='Tracks the percentage of on-time deliveries')),
                ('quality_rating_avg', models.FloatField(help_text='Average rating of quality based on purchase orders')),
                ('average_response_time', models.FloatField(help_text='Average time taken to acknowledge purchase orders')),
                ('fulfillment_rate', models.FloatField(help_text='Percentage of purchase orders fulfilled successfully')),
            ],
        ),
    ]
