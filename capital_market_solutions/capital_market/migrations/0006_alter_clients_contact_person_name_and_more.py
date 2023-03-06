# Generated by Django 4.1.7 on 2023-03-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capital_market', '0005_rename_application_teammembers_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='contact_person_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='primary_email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='primary_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='secondary_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='secondary_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='position',
            field=models.CharField(blank=True, choices=[('Manager', 'Manager'), ('Sr.Software Engineer', 'Sr.Software Engineer'), ('Software Engineer', 'Software Engineer'), ('Jr.Software Engineer', 'Jr.Software Engineer'), ('Intern', 'Intern')], max_length=30),
        ),
        migrations.AlterField(
            model_name='teammembers',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]