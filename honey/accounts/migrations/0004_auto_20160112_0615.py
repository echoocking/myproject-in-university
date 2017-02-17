# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userdetil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Userdetil',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=datetime.datetime(2016, 1, 12, 6, 15, 12, 355412, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 1, 12, 6, 15, 34, 575457, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='sexy',
            field=models.CharField(default=datetime.datetime(2016, 1, 12, 6, 15, 44, 801191, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userdescribe',
            field=models.CharField(default=datetime.datetime(2016, 1, 12, 6, 15, 56, 517033, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
