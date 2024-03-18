# Generated by Django 5.0 on 2024-01-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=50)),
                ('Product_Category', models.CharField(default='', max_length=50)),
                ('Product_SubCategory', models.CharField(max_length=50)),
                ('Product_Price', models.IntegerField(default=0)),
                ('Product_Desc', models.CharField(max_length=300)),
                ('Product_Image', models.ImageField(upload_to='images/image')),
            ],
        ),
    ]
