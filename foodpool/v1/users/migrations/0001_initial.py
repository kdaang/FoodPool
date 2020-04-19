# Generated by Django 3.0.5 on 2020-04-19 18:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address_1', models.CharField(max_length=254)),
                ('address_2', models.CharField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('province', models.CharField(choices=[('NL', 'Newfoundland and Labrador'), ('PE', 'Prince Edward Island'), ('NB', 'Nova Scotia'), ('NS', 'New Brunswick'), ('QC', 'Quebec'), ('ON', 'Ontario'), ('MB', 'Manitoba'), ('SK', 'Saskatchewan'), ('AB', 'Alberta'), ('BC', 'British Columbia'), ('YT', 'Yukon'), ('NT', 'Northwest Territories'), ('NU', 'Nunavut')], max_length=254)),
                ('postal_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(regex='[A-Za-z]\\d[A-Za-z]\\d[A-Za-z]\\d')])),
                ('country', models.CharField(choices=[('CAN', 'Canada')], default='CAN', max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]