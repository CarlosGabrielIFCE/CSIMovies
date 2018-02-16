from django.db import models

class Film(models.Model):

    class Meta:
        db_table = 'film'

    title = models.CharField('Titulo', max_length=100)
    description = models.TextField('Descrição')
    director = models.CharField('Diretor', max_length=100)
    producer = models.CharField('Produtora', max_length=100)
    release_date = models.DateField('Produzido em', blank=True, null=True)
    rt_score = models.IntegerField('Nota')
    image = models.ImageField(upload_to="films/images", verbose_name='Imagem', null=True, blank=True)
    folder_image = models.ImageField(upload_to="films/images", verbose_name='Imagem principal', null=True, blank=True)

    def __str__(self):
        return self.title
