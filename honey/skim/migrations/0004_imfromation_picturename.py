# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skim', '0003_imfromation_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='imfromation',
            name='picturename',
            field=models.FileField(default=b'image/no-img.jpg', upload_to=b'./uplodeimages/'),
        ),
    ]
