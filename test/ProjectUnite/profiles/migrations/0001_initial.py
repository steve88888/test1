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
            name='SignUp',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('userID', models.AutoField(serialize=False, primary_key=True)),
                ('full_name', models.CharField(max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('expertise', models.CharField(max_length=50, choices=[(b'Business and Commerce', b'Business and Commerce'), (b'Architecture, Construction, Urban Design', b'Architecture, Construction, Urban Design'), (b'Fashion & Style', b'Fashion & Style'), (b'Computer Science and Information Technology', b'Computer Science and Information Technology'), (b'Healthcare', b'Healthcare'), (b'Retail & Sales', b'Retail & Sales'), (b'Food & Restaurant', b'Food & Restaurant'), (b'Charity and fundraising organising', b'Charity and fundraising organising'), (b'Research and Theses', b'Research and Theses')])),
                ('location', models.CharField(max_length=50, choices=[(b'Melbourne', b'Melbourne'), (b'Brunswick', b'Brunswick'), (b'WorldWide', b'WorldWide')])),
                ('skills', models.TextField()),
                ('Experience', models.TextField()),
                ('CurrentDegree', models.CharField(max_length=40, null=True, blank=True)),
                ('Currentprojects', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('picture', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
