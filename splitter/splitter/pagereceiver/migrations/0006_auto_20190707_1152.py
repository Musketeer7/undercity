# Generated by Django 2.2.3 on 2019-07-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagereceiver', '0005_auto_20190626_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='first_catch',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='phrase',
            name='ocr',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
