# Generated by Django 4.1.3 on 2022-11-17 05:54

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
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updation_date')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('multianswer', 'multianswer'), ('text', 'text')], max_length=50, verbose_name='type_question')),
                ('text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('is_required', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updation_date')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pub', 'published'), ('un', 'unpublished')], max_length=50, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updation_date')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='admin')),
            ],
        ),
        migrations.CreateModel(
            name='TxtAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txt_ans', models.TextField(blank=True, null=True, verbose_name='text_answer')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updation_date')),
                ('que', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='txtanswertoquestion', to='feedback.question', verbose_name='question')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feedback.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='tracking_code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updation_date')),
                ('answer', models.ManyToManyField(blank=True, to='feedback.choice')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feedback.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feedback.survey'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.question'),
        ),
    ]
