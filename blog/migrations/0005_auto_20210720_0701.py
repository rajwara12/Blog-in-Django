# Generated by Django 3.2.3 on 2021-07-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AddField(
            model_name='post',
            name='sno',
            field=models.AutoField(default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
