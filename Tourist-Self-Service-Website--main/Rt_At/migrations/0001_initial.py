# Generated by Django 5.0.6 on 2024-07-09 02:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Attraction', '0004_alter_attraction_official_phone'),
        ('Route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rt_At',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_routes', to='Attraction.attraction')),
                ('rt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_attractions', to='Route.route')),
            ],
            options={
                'verbose_name': '线路-景点对应表',
                'verbose_name_plural': '线路-景点对应表',
                'db_table': 'rt_at',
            },
        ),
    ]
