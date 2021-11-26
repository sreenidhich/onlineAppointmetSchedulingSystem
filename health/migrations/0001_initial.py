# Generated by Django 3.2.8 on 2021-11-08 21:22

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
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateField(null=True)),
                ('a_timing', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('p_status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('days', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('appoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('-A', '-A'), ('+A', '+A'), ('-B', '-B'), ('+B', '+B'), ('-AB', '-AB'), ('+AB', '+AB'), ('-O', '-O'), ('+O', '+O')], max_length=10, null=True)),
                ('ex_year', models.CharField(max_length=10, null=True)),
                ('ex_month', models.CharField(max_length=10, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medical_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('disc', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('appoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('specialist', models.CharField(max_length=100, null=True)),
                ('service', models.CharField(max_length=100, null=True)),
                ('daystiming', models.CharField(max_length=100, null=True)),
                ('timing', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100, null=True)),
                ('biography', models.TextField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='health.patient'),
        ),
        migrations.CreateModel(
            name='Adminstration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]