from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d/')),
                ('release_date', models.CharField(max_length=15)),
                ('lte_exists', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
        ),
    ]

