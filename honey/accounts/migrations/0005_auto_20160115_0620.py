# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160112_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sexy',
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(default=datetime.datetime(2016, 1, 15, 6, 20, 40, 5943, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
    ]
