# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import aldryn_newsblog.models
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('aldryn_newsblog', '0015_auto_20161208_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsBlogArticlesByCategoryPlugin',
            fields=[
                ('cache_duration', models.PositiveSmallIntegerField(default=0, help_text="The maximum duration (in seconds) that this plugin's content should be cached.")),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('category', models.CharField(default='', help_text='The category of latest articles to display.', max_length=255)),
                ('latest_articles', models.IntegerField(default=5, help_text='The maximum number of latest articles to display.')),
                ('exclude_featured', models.PositiveSmallIntegerField(default=0, help_text='The maximum number of featured articles to exclude from display. E.g. for uses in combination with featured articles plugin.', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(aldryn_newsblog.models.PluginEditModeMixin, 'cms.cmsplugin', models.Model),
        ),
        migrations.AlterField(
            model_name='article',
            name='featured_image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='featured image', blank=True, to=settings.FILER_IMAGE_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='namespace',
            field=models.CharField(default=None, unique=True, max_length=100, verbose_name='Instance namespace'),
        ),
        migrations.AlterField(
            model_name='newsblogconfig',
            name='type',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='newsblogarticlesbycategoryplugin',
            name='app_config',
            field=models.ForeignKey(verbose_name='Apphook configuration', to='aldryn_newsblog.NewsBlogConfig'),
        ),
    ]
