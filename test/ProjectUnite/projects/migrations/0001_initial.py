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
            name='ProjectTitle',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('projectID', models.AutoField(serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=50, choices=[(b'Melbourne', b'Melbourne'), (b'Brunswick', b'Brunswick'), (b'WorldWide', b'WorldWide')])),
                ('contact_email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('team_members', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('expertise', models.CharField(max_length=50, choices=[(b'Business and Commerce', b'Business and Commerce'), (b'Architecture, Construction, Urban Design', b'Architecture, Construction, Urban Design'), (b'Fashion & Style', b'Fashion & Style'), (b'Computer Science and Information Technology', b'Computer Science and Information Technology'), (b'Healthcare', b'Healthcare'), (b'Retail & Sales', b'Retail & Sales'), (b'Food & Restaurant', b'Food & Restaurant'), (b'Charity and fundraising organising', b'Charity and fundraising organising'), (b'Research and Theses', b'Research and Theses')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
