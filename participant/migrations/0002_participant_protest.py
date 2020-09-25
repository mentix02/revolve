# Generated by Django 3.1.1 on 2020-09-25 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('protests', '0001_initial'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='protest',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='participants',
                to='protests.protest',
            ),
        ),
    ]
