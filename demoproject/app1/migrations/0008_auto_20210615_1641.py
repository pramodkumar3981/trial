# Generated by Django 3.2 on 2021-06-15 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_contact_profileusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='profileusers',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.gender'),
        ),
    ]
