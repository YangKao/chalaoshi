# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-06 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.BigIntegerField()),
                ('content', models.TextField()),
                ('status', models.IntegerField(choices=[(0, '未审核'), (1, '已审核'), (-1, '删除'), (2, 'reported')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LogOnSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.BigIntegerField()),
                ('kw', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LogOnTeacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.BigIntegerField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='OpenID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('openid', models.CharField(max_length=100)),
                ('uuid', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.BigIntegerField()),
                ('rate', models.IntegerField()),
                ('check_in', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RateOnComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('uuid', models.BigIntegerField()),
                ('rate', models.IntegerField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SNSVisitLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=50)),
                ('source', models.CharField(max_length=100)),
                ('uuid', models.BigIntegerField()),
                ('path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hot', models.IntegerField(default=0)),
                ('rate', models.FloatField(default=0.0)),
                ('pinyin', models.CharField(max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.College')),
            ],
        ),
        migrations.AddField(
            model_name='rate',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher+', to='www.Teacher'),
        ),
        migrations.AddField(
            model_name='logonteacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Teacher'),
        ),
        migrations.AddField(
            model_name='comment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.Teacher'),
        ),
        migrations.AddField(
            model_name='college',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='www.School'),
        ),
    ]
