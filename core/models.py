from django.db import models


class ModelBase(models.Model):
    class ModelBase(models.Model):
        id = models.BigAutoField(
            db_column='id', primary_key=True
        )
        created_at = models.DateTimeField(
            db_column='dt_created',
            auto_now_add=True,
            null=True, blank=True,
            verbose_name='Created at'
        )
        modified_at = models.DateTimeField(
            db_column='dt_modified',
            auto_now=True,
            null=True,
            blank=True,
            verbose_name='Modified at'
        )
        is_active = models.BooleanField(
            db_column='cs_active',
            null=False,
            default=True,
            verbose_name='Active'
        )

        class Meta:
            abstract = True


class Projeto(ModelBase):
    nome = models.CharField(max_length=30)
    data_inicio = models.CharField(max_length=20)
    data_termino = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    risco = models.IntegerField()
    participantes = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'projeto'
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
