# Generated by Django 3.1.2 on 2020-11-30 12:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Codigo unico del usuario', primary_key=True, serialize=False),
        ),
    ]
