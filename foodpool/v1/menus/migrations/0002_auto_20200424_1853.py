# Generated by Django 3.0.5 on 2020-04-24 18:53

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('dishName', models.TextField()),
                ('description', models.TextField()),
                ('calories', models.IntegerField()),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('weekday', 'from_hour'),
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='menu',
            name='group',
        ),
        migrations.RenameField(
            model_name='menuoptionchoices',
            old_name='maxOptions',
            new_name='maxChoices',
        ),
        migrations.RenameField(
            model_name='menuoptionchoices',
            old_name='minOptions',
            new_name='minChoices',
        ),
        migrations.AddField(
            model_name='menuoptionchoices',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='menuoptions',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='isOpen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='menuoptionchoices',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AddConstraint(
            model_name='menuoptionchoices',
            constraint=models.CheckConstraint(check=models.Q(minChoices__lte=django.db.models.expressions.F('maxChoices')), name='choiceConstraint'),
        ),
        migrations.RenameModel(
            old_name='MenuGroup',
            new_name='MenuGroups',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menus.MenuGroups'),
        ),
        migrations.AlterField(
            model_name='menuoptions',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.MenuItems'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='menus.MenuItems'),
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.AlterUniqueTogether(
            name='menuitems',
            unique_together={('weekday', 'from_hour', 'to_hour')},
        ),
    ]
