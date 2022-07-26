# Generated by Django 3.2.14 on 2022-07-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220725_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='Fishing 2022-07-26 10:21', max_length=200, unique=True),
        ),
    ]
