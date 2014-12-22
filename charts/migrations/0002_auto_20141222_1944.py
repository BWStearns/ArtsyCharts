# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectionmembership',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='collectionmembership',
            name='piece',
        ),
        migrations.DeleteModel(
            name='CollectionMembership',
        ),
        migrations.AddField(
            model_name='artpiece',
            name='price',
            field=models.DecimalField(null=True, max_digits=14, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artcollection',
            name='pieces',
            field=models.ManyToManyField(to=b'charts.ArtPiece'),
        ),
        migrations.AlterField(
            model_name='artpiece',
            name='collections',
            field=models.ManyToManyField(to=b'charts.ArtCollection', null=True),
        ),
    ]
