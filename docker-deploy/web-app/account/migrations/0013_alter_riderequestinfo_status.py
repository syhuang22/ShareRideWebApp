# Generated by Django 4.1.6 on 2023-02-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_riderequestinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderequestinfo',
            name='status',
            field=models.CharField(choices=[('COMPLETE', 'COMPLETE'), ('OPEN', 'OPEN'), ('COMFIRM', 'COMFIRM')], default='OPEN', max_length=20),
        ),
    ]
