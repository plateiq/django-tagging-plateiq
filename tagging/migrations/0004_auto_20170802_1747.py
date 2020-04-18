# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0003_auto_20170423_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(
                unique=True,
                max_length=getattr(settings, 'MAX_TAG_LENGTH', 50),
                verbose_name='name',
                db_index=True),
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='created_at',
            field=models.DateTimeField(null=True, db_index=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='taggeditem',
            name='created_user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
