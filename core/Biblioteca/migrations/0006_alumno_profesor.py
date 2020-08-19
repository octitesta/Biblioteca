# Generated by Django 2.2 on 2020-08-19 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteca', '0005_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Biblioteca.Persona')),
                ('matricula', models.IntegerField()),
            ],
            bases=('Biblioteca.persona',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Biblioteca.Persona')),
                ('num_empleado', models.IntegerField()),
            ],
            bases=('Biblioteca.persona',),
        ),
    ]
