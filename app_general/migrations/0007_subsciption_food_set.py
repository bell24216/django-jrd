# Generated by Django 4.0.4 on 2022-05-04 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0004_rename_special_pricec_food_special_price'),
        ('app_general', '0006_remove_subsciption_food_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsciption',
            name='food_set',
            field=models.ManyToManyField(to='app_foods.food'),
        ),
    ]
