# Generated by Django 4.1.7 on 2023-03-22 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=80)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='restraunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.food')),
                ('restraunt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.restraunt')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.account')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restraunt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zomato.restraunt'),
        ),
    ]
