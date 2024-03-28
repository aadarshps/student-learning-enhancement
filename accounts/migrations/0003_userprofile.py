# Generated by Django 5.0.2 on 2024-03-28 07:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=25)),
                ('mobile_number', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('learning_style', models.CharField(choices=[('visual', 'Visual Learner'), ('auditory', 'Auditory Learner'), ('kinesthetic', 'Kinesthetic Learner')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
                'abstract': False,
            },
        ),
    ]
