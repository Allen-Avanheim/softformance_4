# Generated by Django 4.0.6 on 2022-07-14 07:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking', models.ManyToManyField(blank=True, related_name='tracked_by', to='users.registereduser')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
