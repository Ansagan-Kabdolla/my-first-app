# Generated by Django 2.2.4 on 2020-03-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_auto_20200325_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepdf',
            name='serius',
            field=models.CharField(blank=True, choices=[('mt', 'Математика'), ('ph', 'Физика'), ('bi', 'Биология'), ('ch', 'Химия'), ('pd', 'Педагогика'), ('lt', 'Литература'), ('ek', 'Экономика'), ('pr', 'Право')], default='mt', help_text='Book availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='filepdf',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]