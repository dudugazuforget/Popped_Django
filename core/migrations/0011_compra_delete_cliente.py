# Generated by Django 5.0.6 on 2024-10-02 18:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_cliente_capa_produto_capa"),
    ]

    operations = [
        migrations.CreateModel(
            name="Compra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "status",
                    models.IntegerField(
                        choices=[(1, "Carrinho"), (2, "Realizado"), (3, "Pago"), (4, "Entregue")], default=1
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="compras", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Cliente",
        ),
    ]
