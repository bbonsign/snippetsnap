# Generated by Django 3.0.4 on 2020-03-09 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='code',
            field=models.TextField(default=0, help_text='The code of the snippet'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='copies',
            field=models.PositiveIntegerField(default=0, help_text='Number of times a user has copied the snippet to clipboard'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='language',
            field=models.ForeignKey(default=0, help_text='Programming language of the snippet', on_delete=models.SET('no language available'), related_name='code_snippets', to='snippets.Tag'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(default=0, help_text='The user who owns this snippet', on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snippet',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='The snippet this is forked from', null=True, on_delete=django.db.models.deletion.SET_NULL, to='snippets.Snippet'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=False, help_text='True if the user wants the snippet to be visible to other users'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='tags',
            field=models.ManyToManyField(related_name='snippets', to='snippets.Tag'),
        ),
        migrations.AddField(
            model_name='snippet',
            name='title',
            field=models.CharField(blank=True, help_text='Optional title for the snippet', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='langp',
            field=models.BooleanField(default=False, help_text='True if this tag can be used as a language attribute of a snippet'),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=0, help_text='tag or language applied to a snippet', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
