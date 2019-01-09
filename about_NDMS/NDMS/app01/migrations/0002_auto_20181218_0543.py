# Generated by Django 2.1.1 on 2018-12-17 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='authmode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app01.AuthMode'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app01.Company'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='version',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app01.Version'),
        ),
    ]