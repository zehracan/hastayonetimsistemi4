# Generated by Django 4.0 on 2022-01-02 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_covid_temasli_delete_temaslikisi'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemasliKisi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.personel')),
            ],
        ),
        migrations.AlterField(
            model_name='covid',
            name='temasli',
            field=models.ManyToManyField(blank=True, to='company.TemasliKisi'),
        ),
    ]
