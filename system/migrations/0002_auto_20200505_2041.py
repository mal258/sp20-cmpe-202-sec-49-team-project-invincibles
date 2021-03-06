# Generated by Django 3.0.5 on 2020-05-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(verbose_name='')),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='cost_opt',
            field=models.CharField(choices=[('PER-HOUR', 'PER-HOUR'), ('1-5H', '1-5H'), ('6-10H', '6-10H'), ('PER-DAY', 'PER-DAY')], max_length=50),
        ),
    ]
