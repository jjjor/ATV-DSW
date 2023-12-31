# Generated by Django 4.2.6 on 2023-10-27 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.AddField(
            model_name='city',
            name='state_country',
            field=models.CharField(default=None, max_length=2, verbose_name='Sigla do Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.city', verbose_name='Cidade'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Curso'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
    ]
