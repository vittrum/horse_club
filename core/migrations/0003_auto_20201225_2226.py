# Generated by Django 3.1.3 on 2020-12-25 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('core', '0002_schedule_horse'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='trainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile'),
        ),
        migrations.AddField(
            model_name='clientsubscriptions',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile'),
        ),
        migrations.AddField(
            model_name='clientsubscriptions',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subscription'),
        ),
    ]