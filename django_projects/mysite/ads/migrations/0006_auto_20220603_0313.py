# Generated by Django 3.2.5 on 2022-06-03 03:13

import django.core.validators
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('ads', '0005_alter_ad_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Title must be greater than 2 characters')]),
        ),
    ]
