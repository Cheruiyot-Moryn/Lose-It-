# Generated by Django 4.0.5 on 2022-06-23 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('calorie', models.FloatField(default=0)),
                ('person_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_amount', models.FloatField(blank=True, default=0, null=True)),
                ('amount', models.FloatField(default=0)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorieapp.food')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_count', models.FloatField(blank=True, default=0, null=True)),
                ('quantity', models.FloatField(default=0)),
                ('total_calorie', models.FloatField(default=0, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('calorie_goal', models.PositiveIntegerField(default=0)),
                ('all_food_selected_today', models.ManyToManyField(related_name='inventory', through='calorieapp.PostFood', to='calorieapp.food')),
                ('food_selected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calorieapp.food')),
                ('person_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='postfood',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorieapp.profile'),
        ),
    ]
