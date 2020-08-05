# Generated by Django 2.2.14 on 2020-07-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('M', '0007_grade_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('girl_num', models.IntegerField()),
                ('boy_num', models.IntegerField()),
            ],
            options={
                'db_table': 'company',
            },
        ),
    ]