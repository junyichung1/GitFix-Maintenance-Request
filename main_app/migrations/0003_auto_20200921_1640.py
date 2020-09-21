# Generated by Django 3.1.1 on 2020-09-21 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='unit_id',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.unit'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.unit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]