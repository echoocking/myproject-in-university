# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('userdescribe', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('sexy', models.CharField(max_length=2)),
            ],
        ),
    ]
