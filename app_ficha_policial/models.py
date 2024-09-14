from django.db import models

class FichaPolicial(models.Model):
    id = models.AutoField(primary_key=True)
    grad = models.TextField(blank=True, null=True)
    matr = models.IntegerField(blank=True, null=True, unique=True)  # Adicione unique=True
    nome = models.TextField(blank=True, null=True)
    ome = models.TextField(blank=True, null=True)
    dispo = models.TextField(blank=True, null=True)
    sexo = models.TextField(blank=True, null=True)
    cpf = models.TextField(blank=True, null=True)
    quadro = models.TextField(blank=True, null=True)
    rg = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ficha_policial'