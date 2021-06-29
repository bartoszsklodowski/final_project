# Generated by Django 3.2.3 on 2021-06-27 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='contract',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='contracts.contract'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='employee',
            field=models.ManyToManyField(blank=True, related_name='contracts', to='contracts.Employee'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='contracts.address'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawings', to='contracts.building'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawings', to='contracts.contract'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='technician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawings', to='contracts.employee'),
        ),
        migrations.AlterField(
            model_name='personaldata',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_data', to='contracts.address'),
        ),
        migrations.AlterField(
            model_name='region',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='contracts.address'),
        ),
    ]