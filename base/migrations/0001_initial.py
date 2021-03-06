# Generated by Django 3.2.6 on 2021-09-01 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('postalcode', models.CharField(max_length=200)),
                ('number', models.IntegerField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.city')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.food')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.restaurant')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ManyToManyField(through='base.RestaurantFood', to='base.Restaurant'),
        ),
    ]
