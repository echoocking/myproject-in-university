# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skim', '0004_imfromation_picturename'),
    ]

    operations = [
        migrations.AddField(
            model_name='imfromation',
            name='booknumber',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
