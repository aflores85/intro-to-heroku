# Generated by Django 4.0.4 on 2022-04-26 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0003_alter_discussion_options'),
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'TEMA', 'verbose_name_plural': 'TEMAS'},
        ),
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='discussion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subject', to='discussion.discussion'),
        ),
    ]
