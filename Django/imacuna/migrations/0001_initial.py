# Generated by Django 5.0.3 on 2024-04-02 20:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='facultades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultades',
                'db_table': 'facultades',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='imagenesProyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True)),
                ('imagen', models.ImageField(blank=True, null=True, unique=True, upload_to='imagenesProyectos/', verbose_name='imagen')),
            ],
            options={
                'verbose_name': 'Imágen proyecto',
                'verbose_name_plural': 'Imágenes Proyectos',
                'db_table': 'imagenes_proyecto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Lineas_investigacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('imagen', models.ImageField(null=True, upload_to='iconos/Lineas_investigacion/', verbose_name='imagen')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='rol')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('imagen', models.ImageField(null=True, upload_to='iconos/Servicios/', verbose_name='imagen')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='tipoIntegrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de Integrante',
                'verbose_name_plural': 'Tipos de Integrantes',
                'db_table': 'tipo_integrante',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='videoProyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True)),
                ('archivo_video', models.FileField(unique=True, upload_to='videosProyectos/')),
            ],
            options={
                'verbose_name': 'Video proyecto',
                'verbose_name_plural': 'Videos Proyectos',
                'db_table': 'videos_proyecto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('facultades', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imacuna.facultades')),
            ],
            options={
                'verbose_name': 'Programa',
                'verbose_name_plural': 'Programas',
                'db_table': 'programa',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_apellido', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('segundo_apellido', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('correo', models.CharField(max_length=50, verbose_name='Correo Electrónico')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotoPerfil/')),
                ('linkedin', models.CharField(max_length=100, null=True, verbose_name='urllinkedin')),
                ('resechgate', models.CharField(max_length=100, null=True, verbose_name='urlresechgate')),
                ('facultades', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imacuna.facultades', to_field='nombre')),
                ('programa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imacuna.programa', to_field='nombre')),
                ('tipoIntegrante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imacuna.tipointegrante', to_field='nombre')),
            ],
            options={
                'verbose_name': 'Integrante',
                'verbose_name_plural': 'Integrantes',
                'db_table': 'integrantes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('Completado', models.BooleanField(default=False)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizado', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('imagenesProyectos', models.ManyToManyField(blank=True, to='imacuna.imagenesproyectos', verbose_name='Imágenes')),
                ('integrante', models.ManyToManyField(blank=True, to='imacuna.integrante', verbose_name='Integrantes')),
                ('videoProyectos', models.ManyToManyField(blank=True, to='imacuna.videoproyectos', verbose_name='Videos')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'db_table': 'proyecto',
                'ordering': ['id'],
            },
        ),
    ]
