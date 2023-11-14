# Generated by Django 4.2.7 on 2023-11-14 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=60, verbose_name="Название должности"),
                ),
            ],
            options={
                "verbose_name": "Должность",
                "verbose_name_plural": "Должности",
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "second_name",
                    models.CharField(max_length=60, verbose_name="Фамилия сотрудника"),
                ),
                (
                    "patronymic",
                    models.CharField(
                        max_length=60, null=True, verbose_name="Отчество сотрудника"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=60, verbose_name="Имя сотрудника"),
                ),
                (
                    "date_accept",
                    models.DateField(verbose_name="Дата принятия сотрудника на работу"),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="test_task_app.position",
                        verbose_name="ID должности",
                    ),
                ),
            ],
            options={
                "verbose_name": "Работник",
                "verbose_name_plural": "Работники",
            },
        ),
    ]