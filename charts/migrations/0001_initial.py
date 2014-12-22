# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtCollection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ArtCollection',
                'verbose_name_plural': 'ArtCollections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Unknown', max_length=100)),
                ('birth', models.DateField(null=True)),
                ('death', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArtPiece',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('thumb_url', models.URLField()),
                ('width', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('length', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('height', models.DecimalField(null=True, max_digits=10, decimal_places=3)),
                ('artists', models.ManyToManyField(to='charts.Artist', null=True)),
            ],
            options={
                'verbose_name': 'ArtPiece',
                'verbose_name_plural': 'ArtPieces',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CollectionMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collection', models.ForeignKey(to='charts.ArtCollection')),
                ('piece', models.ForeignKey(to='charts.ArtPiece')),
            ],
            options={
                'verbose_name': 'CollectionMembership',
                'verbose_name_plural': 'CollectionMemberships',
            },
            bases=(models.Model,),
        ),
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
            model_name='artpiece',
            name='collections',
            field=models.ManyToManyField(to='charts.ArtCollection', null=True, through='charts.CollectionMembership'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artpiece',
            name='medium',
            field=models.ForeignKey(to='charts.Medium'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artpiece',
            name='primary_artist',
            field=models.ForeignKey(related_name=b'pieces_as_primary', to='charts.Artist', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artist',
            name='pieces',
            field=models.ManyToManyField(to='charts.ArtPiece'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='artcollection',
            name='pieces',
            field=models.ManyToManyField(to='charts.ArtPiece', through='charts.CollectionMembership'),
            preserve_default=True,
        ),
    ]
