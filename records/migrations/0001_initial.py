# Generated by Django 4.1.5 on 2023-01-27 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_on', models.DateTimeField(auto_now_add=True)),
                ('asset_status', models.CharField(blank=True, choices=[('a', 'Available'), ('n', 'Needs Maintenance'), ('d', 'Discontinued'), ('r', 'Returned'), ('x', 'Assigned')], default='a', help_text='Asset Availability', max_length=1)),
                ('asset_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.asset')),
            ],
        ),
    ]
