from __future__ import unicode_literals

from django.cong import settings
from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MushroomSpot',
            fields=[
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
    ]