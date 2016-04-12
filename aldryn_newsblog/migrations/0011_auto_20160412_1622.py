# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_newsblog', '0010_auto_20160316_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsblogconfig',
            name='exclude_featured',
            field=models.PositiveSmallIntegerField(default=0, help_text='If you are using featured articles plugin on article list page you might want to avoid duplicated articles. This option allows you to exclude first N of them.', verbose_name='Excluded featured articles count', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsbloglatestarticlesplugin',
            name='exclude_featured',
            field=models.PositiveSmallIntegerField(default=0, help_text='The maximum number of featured articles to exclude from display. F.e. for uses in combination with featured articles plugin.', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='lead_in',
            field=djangocms_text_ckeditor.fields.HTMLField(default='', help_text='The lead gives the reader the main idea of the story, this is useful in overviews, lists or as an introduction to your article.', verbose_name='lead', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='template_prefix',
            field=models.CharField(max_length=20, null=True, verbose_name='Prefix for template dirs', blank=True),
            preserve_default=True,
        ),
    ]
