# Generated by Django 4.0.3 on 2022-03-09 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklepApp', '0044_rename_user_koszyk_login_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='koszyk_login',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='adres_id',
            new_name='adres',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='email_id',
            new_name='email',
        ),
    ]