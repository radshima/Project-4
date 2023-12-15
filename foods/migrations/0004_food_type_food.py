# Generated by Django 5.0 on 2023-12-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_food_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='type_food',
            field=models.CharField(choices=[('A', 'appetizers'), ('M', 'main dishes'), ('DI', 'desserts'), ('DR', 'drinks')], default='M', max_length=10),
        ),
    ]