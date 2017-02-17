# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skim', '0002_auto_20160103_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='imfromation',
            name='username',
            field=models.CharField(default=datetime.datetime(2016, 1, 3, 5, 25, 30, 493261, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
