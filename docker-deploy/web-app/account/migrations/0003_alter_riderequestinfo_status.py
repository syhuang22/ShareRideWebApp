# Generated by Django 4.1.5 on 2023-02-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_riderequestinfo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riderequestinfo',
            name='status',
            field=models.CharField(choices=[('OPEN', 'OPEN'), ('COMFIRM', 'COMFIRM'), ('COMPLETE', 'COMPLETE')], default='OPEN', max_length=20),
        ),
    ]
