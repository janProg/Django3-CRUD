# Generated by Django 3.1.7 on 2021-03-17 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[('Riding', 'Riding'), ('Other sports', 'Other sports'), ('Basketball', 'Basketball'), ('Soccer', 'Soccer'), ('Swimming', 'Swimming'), ('Hiking', 'Hiking'), ('Tennis', 'Tennis'), ('Running', 'Running'), ('Golf', 'Golf'), ('Baseball', 'Baseball')], max_length=100)),
                ('duration', models.CharField(choices=[('1 hour', '1 hour'), ('30 min', '30 min'), ('2 hours', '2 hours'), ('1 hour 30 min', '1 hour 30 min'), ('longer than 2 hours', 'longer than 2 hours')], max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('feedback', models.CharField(choices=[('Average', 'Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], max_length=100)),
            ],
        ),
    ]