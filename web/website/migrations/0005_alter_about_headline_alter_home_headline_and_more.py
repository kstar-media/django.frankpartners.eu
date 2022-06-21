# Generated by Django 4.0.4 on 2022-06-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_about_home_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='headline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='home',
            name='headline',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='headline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service1_headline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service1_icon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service2_headline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service2_icon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service3_headline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service3_icon',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='bio',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='firstname',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='lastname',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='since',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='values',
            name='headline',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]