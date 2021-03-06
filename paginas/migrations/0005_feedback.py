# Generated by Django 4.0 on 2021-12-21 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('paginas', '0004_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(choices=[('Sugestâo', 'Sugestão'), ('Reclamação', 'Reclamação'), ('Parceria', 'Parceria'), ('Outro', 'Outro')], max_length=10)),
                ('descricao', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
