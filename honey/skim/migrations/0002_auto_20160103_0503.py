# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skim', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imfromation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bookname', models.CharField(max_length=1000)),
                ('classify', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('discribe', models.CharField(max_length=10000000)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
