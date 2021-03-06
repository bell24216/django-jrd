# Generated by Django 4.0.4 on 2022-05-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0004_rename_special_pricec_food_special_price'),
        ('app_general', '0007_subsciption_food_set'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=15, unique=True)),
                ('status', models.CharField(choices=[('unapproved', 'Unapproced'), ('approved', 'Approced'), ('benned', 'Benned')], default='unapproved', max_length=15)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
                ('food_set', models.ManyToManyField(to='app_foods.food')),
            ],
        ),
        migrations.DeleteModel(
            name='Subsciption',
        ),
    ]
