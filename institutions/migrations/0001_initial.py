# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=200)),
                ('abbr', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('abbr',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='area',
            name='institution',
            field=models.ForeignKey(to='institutions.Institution'),
            preserve_default=True,
        ),
    ]
