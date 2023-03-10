# Generated by Django 4.1.5 on 2023-01-27 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(max_length=100)),
                ('asset_code', models.CharField(help_text='Enter Number engraved on the Asset', max_length=100)),
                ('asset_model', models.CharField(max_length=100)),
                ('purchase_value', models.CharField(default='0', max_length=200)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('n', 'Needs Maintenance'), ('d', 'Discontinued'), ('r', 'Reserved'), ('x', 'Assigned')], default='a', help_text='Asset Availability', max_length=2)),
            ],
            options={
                'ordering': ('asset_type', 'date_added'),
            },
        ),
    ]
