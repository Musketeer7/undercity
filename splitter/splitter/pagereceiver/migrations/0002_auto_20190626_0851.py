# Generated by Django 2.2.2 on 2019-06-26 08:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pagereceiver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 8, 51, 18, 909445, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='file',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 26, 8, 51, 18, 909470, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('ocr', models.CharField(max_length=30)),
                ('first_catch', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 8, 51, 18, 928486, tzinfo=utc), editable=False)),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2019, 6, 26, 8, 51, 18, 928508, tzinfo=utc))),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagereceiver.File')),
            ],
        ),
    ]
