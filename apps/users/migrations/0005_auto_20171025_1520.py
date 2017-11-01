# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171025_1504'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmaiVerifyRecord',
            new_name='EmailVerifyRecord',
        ),
    ]
