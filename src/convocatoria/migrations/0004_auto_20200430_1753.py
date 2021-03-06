# Generated by Django 3.0.5 on 2020-04-30 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convocatoria', '0003_auto_20200430_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postulacion',
            name='convocatoria',
        ),
        migrations.RemoveField(
            model_name='postulacionanonima',
            name='convocatoria',
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='anonymous_applications',
            field=models.ManyToManyField(to='convocatoria.PostulacionAnonima'),
        ),
        migrations.AddField(
            model_name='convocatoria',
            name='candidate_applications',
            field=models.ManyToManyField(to='convocatoria.Postulacion'),
        ),
    ]
