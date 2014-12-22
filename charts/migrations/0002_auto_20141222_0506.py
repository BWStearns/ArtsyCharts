# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Medium',
                'verbose_name_plural': 'Media',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artist',
            name='birth',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='death',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='name',
            field=models.CharField(default=b'Unknown', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artpiece',
            name='medium',
            field=models.ForeignKey(default=0, to='charts.Medium'),
            preserve_default=False,
        ),
    ]
