# Generated by Django 4.1.1 on 2022-10-04 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livros',
            old_name='author',
            new_name='Autor',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='coauthor',
            new_name='Coautor',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='edition',
            new_name='Edicao',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='name',
            new_name='Nome',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='type',
            new_name='Tipo',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='title',
            new_name='Titulo',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='date',
            new_name='data',
        ),
    ]
