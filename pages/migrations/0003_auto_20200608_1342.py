# Generated by Django 3.0.7 on 2020-06-08 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200608_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]