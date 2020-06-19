from django.db import models
import uuid
import os

# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s"%(uuid.uuid4(),ext)
    return os.path.join("produtos",filename)

class Categoria(models.Model):
    nome = models.CharField(max_length=255,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):

    VALORES = (
        ('P','P'),
        ('M','M'),
        ('G','G'),
        ('GG','GG'),
    )

    nome = models.CharField(max_length=255,null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2,null=False)
    quantidade = models.PositiveIntegerField(null=False)
    descricao = models.TextField(null=False)
    tamanho = models.CharField(max_length=2,choices=VALORES,default='M')
    foto1 = models.FileField(upload_to=get_file_path,null=True)
    foto2 = models.FileField(upload_to=get_file_path,null=True)
    foto3 = models.FileField(upload_to=get_file_path,null=True)
    categoria = models.ForeignKey(
                    Categoria,
                    on_delete=models.SET_NULL,
                    blank=True,
                    null=True,
                )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


