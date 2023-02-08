# Generated by Django 4.1.6 on 2023-02-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bootcamp_grad',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='cs_degree',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='figma_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='github_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='google_drive_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='industry_prof',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='jira_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='microsoft_teams_links',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='portfolio_link',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('FS', 'FullStack'), ('FE', 'FrontEnd'), ('BE', 'BackEnd'), ('UX', 'UX/UI Designer')], default='FS', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='self_taught',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='slack_link',
            field=models.CharField(default='URL', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='tools',
            field=models.TextField(default='Python'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='trello_link',
            field=models.CharField(default='URL', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.CharField(default='URL', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='zoom_link',
            field=models.CharField(default='URL', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='roles',
            field=models.TextField(default='Lead'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.TextField(default='Python'),
            preserve_default=False,
        ),
    ]
