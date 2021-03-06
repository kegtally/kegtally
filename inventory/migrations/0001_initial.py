# Generated by Django 2.0.2 on 2018-03-31 19:04

import common.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('created', common.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', common.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('litres', models.IntegerField(default=1000)),
            ],
            options={
                'verbose_name': 'batch',
                'verbose_name_plural': 'batches',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('created', common.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', common.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('qbid', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'beer',
                'verbose_name_plural': 'beers',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Fill',
            fields=[
                ('created', common.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', common.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('qbid', models.IntegerField(null=True)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch', to='inventory.Batch')),
            ],
            options={
                'verbose_name': 'keg fill',
                'verbose_name_plural': 'keg fills',
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Keg',
            fields=[
                ('created', common.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', common.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('litres', models.IntegerField(choices=[(50, '50 Litres'), (30, '30 Litres'), (20, '20 Litres')], default=50)),
            ],
            options={
                'verbose_name': 'keg',
                'verbose_name_plural': 'kegs',
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='fill',
            name='keg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keg', to='inventory.Keg'),
        ),
        migrations.AddField(
            model_name='batch',
            name='beer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='beer', to='inventory.Beer'),
        ),
    ]
