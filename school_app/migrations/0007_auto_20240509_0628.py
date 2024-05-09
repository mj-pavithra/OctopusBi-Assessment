# Generated by Django 3.2.12 on 2024-05-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0006_auto_20240509_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='student_area_assessed_score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='summary',
            name='sydney_average_score',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
