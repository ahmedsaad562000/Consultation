# Generated by Django 4.1.4 on 2022-12-23 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0004_rename_user_acc_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='acc_User',
            new_name='User',
        ),
    ]
