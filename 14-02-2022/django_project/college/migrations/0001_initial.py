# Generated by Django 4.0 on 2022-02-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='college_model',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('Kannada', models.IntegerField(max_length=100)),
                ('English', models.IntegerField(max_length=100)),
                ('Hindhi', models.IntegerField(max_length=100)),
                ('Maths', models.IntegerField(max_length=100)),
                ('Science', models.IntegerField(max_length=100)),
                ('Social', models.IntegerField(max_length=100)),
            ],
        ),
    ]
