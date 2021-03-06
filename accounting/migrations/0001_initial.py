# Generated by Django 2.0.2 on 2018-04-11 01:48

import common.fields
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('created', common.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', common.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('qbid', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
                'ordering': ('created',),
            },
        ),
    ]
