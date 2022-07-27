# Generated by Django 4.0.4 on 2022-07-21 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basepost')),
            ],
            bases=('core.basepost',),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basepost')),
            ],
            bases=('core.basepost',),
        ),
    ]
